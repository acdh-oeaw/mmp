import requests
from story_map.models import Slide, Story


def fetch_data_from_knightlab(url):
    r = requests.get(url)
    data = r.json()
    return data['storymap']


def enrich_story(story, story_data):
    for x in [
        'attribution',
        'call_to_action',
        'language',
        'map_background_color',
        'map_subdomains',
        'map_type',
    ]:
        try:
            setattr(story, x, story_data[x])
        except KeyError:
            pass
    if story_data['zoomify']:
        for x in [
            'path', 'height', 'width', 'attribution'
        ]:
            setattr(story, f"zoomify_{x}", story_data['zoomify'][x])
    story.save()
    return story


def save_slides(data, story_title='default story'):
    story, _ = Story.objects.get_or_create(title=story_title)
    story.has_slides.all().delete()
    enrich_story(story, data)
    items = []
    for i, x in enumerate(data['slides']):
        order_nr = i + 1
        item = Slide.objects.create(
            story=story,
            order_nr=order_nr,
            text_headline=x['text']['headline'],
            media_caption=x['media']['caption'],
            media_credit=x['media']['credit'],
            media_url=x['media']['url'],
        )
        try:
            item.text_text = x['text']['text']
        except KeyError:
            pass
        try:
            item.location_lat = x['location']['lat']
            item.location_lng = x['location']['lon']
        except KeyError:
            pass
        item.save()
        items.append(item)
    return(items)


def import_from_knlab(url, story_title):
    data = fetch_data_from_knightlab(url)
    items = save_slides(data, story_title)
    return items
