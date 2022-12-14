import pandas as pd

from archiv.models import KeyWord, logger


generic_property_table = [
    ("stichwort", "s"),
    ("id", "s_id"),
    ("art", "art"),
    ("rvn_stelle_key_word_keyword__id", "stelle_id"),
    ("rvn_stelle_key_word_keyword__key_word__stichwort", "t"),
    ("rvn_stelle_key_word_keyword__key_word__id", "t_id"),
    ("rvn_stelle_key_word_keyword__key_word__art", "t_art"),
]


def graph_table(stellen, prop_table=generic_property_table):
    """takes a qs and returns a 'edge' df"""
    property_table = prop_table
    qs = KeyWord.objects.filter(rvn_stelle_key_word_keyword__in=stellen).distinct()
    logger.info(
        f"compiling network for {qs.count()} KeyWords mentioned in {stellen.count()} Stellen"
    )
    columns = [x[1] for x in property_table]
    props = [x[0] for x in property_table]

    df = pd.DataFrame(list(qs.values_list(*props)), columns=columns)
    df = df[df["s_id"] > df["t_id"]]
    return df


def create_graph(df):
    graph = {}
    df["edge_key"] = df.apply(
        lambda row: f"keyword_{row['s_id']}__keyword_{row['t_id']}", axis=1
    )
    nodes = {}
    graph['edges'] = []
    for g, ndf in df.groupby('edge_key'):
        source_id, target_id = g.split("__")
        edge = {
            "key": g,
            "source": f"keyword__{source_id}",
            "target": f"keyword__{target_id}",
            "passage_ids": [int(x) for x in sorted(list(set(ndf['stelle_id'].values)))],
            "count": len(ndf)
        }
        nodes[f"{source_id}"] = {
            "key": f"{source_id}",
            "id": int(ndf.iloc[0]['s_id']),
            "kind": "keyword",
            "type": ndf.iloc[0]['art'],
            "label": ndf.iloc[0]['s'],
        }
        nodes[f"{target_id}"] = {
            "key": f"{target_id}",
            "id": int(ndf.iloc[0]['t_id']),
            "kind": "keyword",
            "type": ndf.iloc[0]['t_art'],
            "label": ndf.iloc[0]['t'],
        }
        graph["edges"].append(edge)
    graph["nodes"] = [value for key, value in nodes.items()]
    return graph
