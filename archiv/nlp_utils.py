import itertools
from collections import Counter
from django.contrib.contenttypes.models import ContentType


def get_nlp_data(qs):
    stop_word_ct = ContentType.objects.get(app_label='topics', model='stopword')
    stop_word_class = stop_word_ct.model_class()
    stop_words = [x[0] for x in stop_word_class.objects.all().values_list('word')]
    qs_filtered = qs.exclude(lemmata__isnull=True).filter(text__text_lang='lat')
    try:
        tokens = [
            x['lemma'] for x in list(
                itertools.chain(*[x.lemmata['processed_text'] for x in qs_filtered])
            ) if x['token'] not in stop_words
        ]
    except TypeError:
        tokens = []
    if tokens:
        tokens = [
            x for x in tokens if x not in stop_words
        ]
    token_dict = dict(Counter(tokens))
    return {
        "token": tokens,
        "token_dict": token_dict,
        "token_count": len(tokens),
        "unique_token_count": len(set(tokens))
    }
