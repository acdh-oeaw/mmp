import spacy

nlp = spacy.load("la_core_cltk_sm")


def process_text(my_text, lang_model=nlp):
    doc = lang_model(my_text)
    result = {}
    processed_text = []
    for x in doc:
        if x.is_stop or x.is_space or x.is_punct or x.is_digit:
            continue
        else:
            item = {
                'token': x.text,
                'pos': f"{x.pos_}",
                'lemma': x.lemma_.lower()
            }
            processed_text.append(item)
    result['orig_text'] = my_text
    result['tokens'] = [x['token'] for x in processed_text]
    result['processed_text'] = processed_text
    return result
