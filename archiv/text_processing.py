import cltk
from cltk import NLP
cltk_nlp_lat = NLP(language="lat", suppress_banner=True)
to_remove = [
    cltk.lexicon.processes.LatinLexiconProcess,
    cltk.embeddings.processes.LatinEmbeddingsProcess,
]
for x in to_remove:
    cltk_nlp_lat.pipeline.processes.remove(x)


def process_text(my_text, lang_model=cltk_nlp_lat):
    cltk_doc = lang_model.analyze(text=my_text)
    result = {}
    processed_text = [
        {
            'token': x.string,
            'pos': f"{x.pos}",
            'lemma': x.lemma,
            'named_entity': x.named_entity,
            'index_sentence': x.index_sentence,
            'stop_word': x.stop
        } for x in cltk_doc.words
    ]
    result['orig_text'] = my_text
    result['tokens'] = [
        x['lemma'].lower() for x in processed_text if x['pos'] != 'punctuation' and not x['stop_word']
    ]
    result['NER'] = [
        {
            'ner_type': x['named_entity'], 'ner': x['lemma']
        } for x in processed_text if x['named_entity']
    ]
    result['processed_text'] = processed_text
    return result
