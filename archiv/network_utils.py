import pandas as pd


generic_property_table = [
    ('stichwort', 's'),
    ('id', 's_id'),
    ('rvn_stelle_key_word_keyword__id', 'stelle_id'),
    ('rvn_stelle_key_word_keyword__key_word__stichwort', 't'),
    ('rvn_stelle_key_word_keyword__key_word__id', 't_id')
]


def graph_table(qs, prop_table=generic_property_table):
    """ takes a qs and returns a 'edge' df """
    property_table = prop_table
    columns = [x[1] for x in property_table]
    props = [x[0] for x in property_table]

    df = pd.DataFrame(
        list(qs.values_list(*props)),
        columns=columns
    )
    df = df[df['s_id'] > df['t_id']]
    return df


def create_graph(df, qs):
    edges = []
    nodes = []
    for i, row in df.iterrows():
        edges.append(
            {
                "id": i,
                "source": row['s_id'],
                "target": row['t_id'],
                "type": 'e'
            }
        )
    for x in qs:
        nodes.append(
            {
                "id": x.id,
                "label": x.stichwort,
                "type": 'n'
            }
        )
    for i, row in df.groupby(['t_id', 't']).size().reset_index(name="occ").iterrows():
        nodes.append(
            {
                "id": row['t_id'],
                "label": row['t'],
                "type": 'n'
            }
        )
    g_types = {
        "nodes": [
            {
                'id': 'n',
                'label': 'Keyword',
                'color': '#006699'
            },
        ],
        "edges": [
            {
                "id": 'e',
                "color": '#990066'
            }
        ]
    }
    graph = {
        "nodes": nodes,
        "edges": edges,
        "types": g_types
    }
    return graph
