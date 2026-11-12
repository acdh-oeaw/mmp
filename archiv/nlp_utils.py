from collections import Counter

from topics.models import StopWord


def get_nlp_data(qs):
    stop_words = set(StopWord.objects.values_list("word", flat=True))
    qs_filtered = qs.exclude(lemmata__isnull=True).filter(text__text_lang="lat")
    try:
        tokens = [
            x["lemma"]
            for lemmata in qs_filtered.values_list("lemmata", flat=True).iterator()
            for x in lemmata["processed_text"]
            if x["token"] not in stop_words
        ]
    except TypeError:
        tokens = []
    if tokens:
        tokens = [x for x in tokens if x not in stop_words]
    token_dict = dict(Counter(tokens))
    return {
        "token": tokens,
        "token_dict": token_dict,
        "token_count": len(tokens),
        "unique_token_count": len(set(tokens)),
    }
