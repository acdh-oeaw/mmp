import itertools
from collections import Counter


def get_nlp_data(qs):
    qs_filtered = qs.exclude(lemmata__isnull=True).filter(text__text_lang='lat')
    try:
        tokens = [
            x['lemma'] for x in list(
                itertools.chain(*[x.lemmata['processed_text'] for x in qs_filtered])
            )
        ]
    except TypeError:
        tokens = []
    token_dict = dict(Counter(tokens))
    return {
        "token": tokens,
        "token_dict": token_dict,
        "token_count": len(tokens),
        "unique_token_count": len(set(tokens))
    }
