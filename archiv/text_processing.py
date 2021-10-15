import cltk
from cltk import NLP
cltk_nlp_lat = NLP(language="lat")
to_remove = [
    cltk.lexicon.processes.LatinLexiconProcess,
    cltk.embeddings.processes.LatinEmbeddingsProcess,
]
for x in to_remove:
    cltk_nlp_lat.pipeline.processes.remove(x)


def process_text(my_text, lang_model=cltk_nlp_lat):
    cltk_doc = lang_model.analyze(text=my_text)
    processed_text = [
        {
            'token': x.string,
            'pos': x.pos,
            'lemma': x.lemma,
            'named_entity': x.named_entity,
            'index_sentence': x.index_sentence
        } for x in cltk_doc.words
    ]
    return processed_text
