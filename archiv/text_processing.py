import stanza

nlp = stanza.Pipeline('la', processors='tokenize,pos,lemma')


def process_text(my_text, lang_model=nlp):
    doc = nlp(my_text)
    result = {}
    processed_text = []
    for sent in doc.sentences:
        for x in sent.words:
            if x.pos == 'PUNCT':
                continue
            else:
                item = {
                    'token': x.text,
                    'pos': f"{x.pos}",
                    'lemma': x.lemma,
                }
                processed_text.append(item)
    result['orig_text'] = my_text
    result['tokens'] = [x['token'] for x in processed_text]
    result['processed_text'] = processed_text
    return result
