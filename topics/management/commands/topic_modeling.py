from datetime import datetime
import pandas as pd
from django.core.management.base import BaseCommand
from tqdm import tqdm

from gensim.corpora import Dictionary
from gensim.models import LdaModel

from archiv.models import Stelle
from topics.models import ModelingProcess, Topic, TextTopicRelation
from topics.utils import top_to_topic_object


class Command(BaseCommand):
    help = "Run Topic Modeling and save results"

    def handle(self, *args, **kwargs):
        print("deleting previous Topics")
        ModelingProcess.objects.all().delete()
        TextTopicRelation.objects.all().delete()
        qs = Stelle.objects.filter(lemmata__isnull=False).filter(text__text_lang='lat')
        process_start = datetime.now()
        params = {
            "LdaModel_params": {
                "num_topics": 10,
                "chunksize": 2000,
                "passes": 20,
                "iterations": 40,
                "eval_every": None,
                "alpha": "auto",
                "eta": "auto",
            },
            "dict_filter_params": {
                "no_below": 2,
                "no_above": 0.5
            }
        }
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
        _ = dictionary[0]  # This is only to "load" the dictionary.
        id2word = dictionary.id2token
        model = LdaModel(
            corpus=corpus,
            id2word=id2word,
            **params["LdaModel_params"]
        )
        model_process = ModelingProcess.objects.create(
            process_start=process_start,
            process_end=datetime.now(),
            param=params
        )
        topics = model.top_topics(corpus)
        for i, x in enumerate(topics):
            Topic.objects.create(
                topic_index=i,
                process=model_process,
                **top_to_topic_object(x)
            )
        for i, x in tqdm(enumerate([model.get_document_topics(item) for item in corpus]), total=len(df)):
            text_id = df.iloc[i]['db_id']
            text = Stelle.objects.get(id=text_id)
            for topic in x:
                TextTopicRelation.objects.create(
                    text=text,
                    topic=Topic.objects.get(topic_index=topic[0]),
                    weight=topic[1]
                )
