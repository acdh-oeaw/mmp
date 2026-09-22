import json

from django.db import models
from functools import cached_property

# Create your models here.


def xstr(s):
    if s is None:
        return ''
    return str(s)


class Story(models.Model):
    title = models.CharField(
        max_length=250
    )
    attribution = models.CharField(
        blank=True,
        null=True,
        max_length=250
    )
    call_to_action = models.BooleanField(
        default=True
    )
    call_to_action_text = models.CharField(
        blank=True,
        null=True,
        max_length=250
    )
    language = models.CharField(
        default="en",
        max_length=2
    )
    map_background_color = models.CharField(
        default="#5f9468",
        max_length=15
    )
    map_subdomains = models.CharField(
        blank=True,
        null=True,
        max_length=25
    )
    map_type = models.CharField(
        blank=True,
        null=True,
        max_length=25
    )
    zoomify_path = models.CharField(
        blank=True,
        null=True,
        max_length=250
    )
    zoomify_height = models.PositiveSmallIntegerField(
        blank=True,
        null=True
    )
    zoomify_width = models.PositiveSmallIntegerField(
        blank=True,
        null=True
    )
    zoomify_attribution = models.CharField(
        blank=True,
        null=True,
        max_length=250
    )

    def __str__(self):
        return f"{self.title}"

    @cached_property
    def payload(self):
        item = {
            'slides': [],
            'zoomify': {
                'path': xstr(self.zoomify_path),
                'height': self.zoomify_height,
                'width': self.zoomify_width,
                'attribution': xstr(self.attribution)
            },
            'attribution': xstr(self.attribution),
            'call_to_action': self.call_to_action,
            'call_to_action_text': xstr(self.call_to_action_text),
            'language': self.language,
            'map_as_image': False,
            'map_background_color': self.map_background_color,
            'map_subdomains': xstr(self.map_subdomains),
            'map_type': xstr(self.map_type)
        }
        for x in self.has_slides.all():
            item['slides'].append(x.payload)
        return {
            "storymap": item
        }

    @cached_property
    def payload_as_json(self):
        return json.dumps(self.payload)


class Slide(models.Model):
    story = models.ForeignKey(
        'Story',
        on_delete=models.CASCADE,
        related_name="has_slides"
    )
    order_nr = models.PositiveSmallIntegerField(
        help_text="Use this number for ordering your slides"
    )
    location_lat = models.FloatField(
        blank=True,
        null=True
    )
    location_lng = models.FloatField(
        blank=True,
        null=True
    )
    location_zoom = models.PositiveSmallIntegerField(
        default=4
    )
    location_icon_size_l = models.PositiveSmallIntegerField(
        default=48
    )
    location_icon_size_w = models.PositiveSmallIntegerField(
        default=48
    )
    location_line = models.BooleanField(
        default=True
    )
    text_headline = models.CharField(
        max_length=250
    )
    text_text = models.TextField(
        blank=True,
        null=True,
    )
    date = models.DateField(
        blank=True,
        null=True
    )
    media_caption = models.CharField(
        blank=True,
        null=True,
        max_length=250
    )
    media_credit = models.CharField(
        blank=True,
        null=True,
        max_length=250
    )
    media_url = models.URLField(
        blank=True,
        null=True,
        max_length=250
    )

    class Meta:

        ordering = [
            'order_nr',
        ]

    def save(self, *args, **kwargs):
        if self.media_url:
            if self.media_url.startswith('//'):
                self.media_url = self.media_url.replace('//', 'https://')
        super(Slide, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.story.title}__{self.order_nr} {self.text_headline}"

    @property
    def location(self):
        if self.location_lat:
            item = {
                "iconSize": [
                    self.location_icon_size_w, self.location_icon_size_l
                ],
                "lat": self.location_lat,
                "line": self.location_line,
                "lon": self.location_lng,
                "zoom": self.location_zoom
            }
        else:
            item = {
                "line": self.location_line,
            }
        return item

    @property
    def text(self):
        item = {
            "headline": self.text_headline,
            "text": self.text_text
        }
        return item

    @property
    def payload(self):
        if self.date:
            date = f"{self.date}"
        else:
            date = ""
        item = {
            "background": {},
            "date": f"{date}",
            "location": self.location,
            "media": {
                "caption": self.media_caption,
                "credit": self.media_credit,
                "url": self.media_url
            },
            "text": self.text
        }
        if self.location_lng:
            return item
        else:
            item['type'] = "overview"
            return item
