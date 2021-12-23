from topics.models import StopWord

stop_words = [x[0] for x in StopWord.objects.all().values_list('word')]


def top_to_topic_object(topic):
    words = [{x[1]: float(x[0])} for x in topic[0]]
    title = " | ".join([x[1] for x in topic[0][:3]])
    return {
        "word": words,
        "title": title,
        "weight": float(topic[1])
    }
