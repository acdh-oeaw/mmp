import pandas as pd

from netvis.utils import as_node

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


def create_graph(df, ItemClass):
    app_name = ItemClass._meta.app_label
    model_name = ItemClass._meta.model_name
    all_ids = df[['s_id', 't_id']].values.tolist()
    ids = list(set([item for sublist in all_ids for item in sublist]))
    qs = ItemClass.objects.filter(id__in=ids)
    edges = []
    nodes = []
    for i, row in df.iterrows():
        edges.append(
            {
                "id": i,
                "source": f"{app_name}__{model_name}__{row['s_id']}",
                "target": f"{app_name}__{model_name}__{row['t_id']}",
                "type": 'e'
            }
        )
    for x in qs:
        node = as_node(x)
        nodes.append(
            node
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
