from django.core.management.base import BaseCommand
import pandas as pd

from gensim.corpora import Dictionary
from gensim.models import LdaModel

from archiv.models import Stelle
from topics.models import ModelingProcess, Topic


class Command(BaseCommand):
    help = "Creates a document-topic-matrix"

    def handle(self, *args, **kwargs):
        params = {
            "LdaModel_params": {
                "num_topics": 10,
                "chunksize": 2000,
                "passes": 20,
                "iterations": 400,
                "eval_every": None,
                "alpha": "auto",
                "eta": "auto",
            },
            "dict_filter_params": {
                "no_below": 20,
                "no_above": 0.5
            }
        }
        ModelingProcess.objects.all().delete()
        qs = Stelle.objects.filter(lemmata__isnull=False).filter(text__text_lang='lat')
        print(f"Processing {qs.count()} out of {Stelle.objects.all().count()} passages")
        df = pd.DataFrame(
            [
                {
                    'index': i,
                    'db_id': x.id,
                    'text': x.lemmata['tokens']
                } for i, x in enumerate(qs)
            ]
        )
        docs = list(df['text'].values)
        dictionary = Dictionary(docs)
        dictionary.filter_extremes(**params["dict_filter_params"])
        corpus = [dictionary.doc2bow(doc) for doc in docs]
        print(f"Number of unique tokens: {len(dictionary)}")
        print(f"Number of documents: {len(corpus)}")
        dictionary[0]  # This is only to "load" the dictionary.
        id2word = dictionary.id2token
        model = LdaModel(
            corpus=corpus,
            id2word=id2word,
            **params["LdaModel_params"]
        )
        print(model.top_topics(corpus))
