from django.db import models


def set_extra(self, **kwargs):
    self.extra = kwargs
    return self


models.Field.set_extra = set_extra


class GeoJsonLayer(models.Model):
    title = models.CharField(
        max_length=250,
        verbose_name="Title",
        help_text="Title of this Layer",
    ).set_extra(
        is_public=True,
        arche_prop="hasTitle",
    )
    attribution = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Attribution",
        help_text="Attribution to the Layer creator",
    ).set_extra(
        is_public=True,
        arche_prop="hasTitle",
    )
    description = models.TextField(
        blank=True, null=True,
        verbose_name="Description",
        help_text="Short Description of the Use Case",
    ).set_extra(
        is_public=True,
        arche_prop="hasDescription",
    )
    data = models.JSONField(
        verbose_name="GeoJson",
        help_text="The actual GeoJson",
    )

    class Meta:

        ordering = [
            'title',
        ]
        verbose_name = "GeoJson Layer"

    def __str__(self):
        return self.title
