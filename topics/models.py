from django.db import models

from archiv.models import Stelle


class ModelingProcess(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    process_start = models.DateTimeField()
    process_end = models.DateTimeField()
    modeling_type = models.CharField(max_length=250, default="gensim.models.LdaModel")
    param = models.JSONField()

    def __str__(self):
        return f"{self.modeling_type}, created: {self.created_at}"


class Topic(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    word = models.JSONField()
    title = models.CharField(max_length=250)
    weight = models.FloatField(blank=True, null=True)
    process = models.ForeignKey(
        'ModelingProcess', on_delete=models.CASCADE
    )
    topic_index = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}"


class TextTopicRelation(models.Model):
    text = models.ForeignKey(
        Stelle,
        null=True,
        on_delete=models.SET_NULL,
        related_name='has_topics'
    )
    topic = models.ForeignKey(
        Topic,
        null=True,
        on_delete=models.SET_NULL,
        related_name='has_related_texts'
    )
    weight = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.text} <> {self.topic}"


class StopWord(models.Model):
    word = models.CharField(
        blank=True,
        null=True,
        max_length=250,
        verbose_name="stop word",
        help_text="Word/Token to be excluded from any processing"
    )

    def __str__(self):
        return f"{self.word}"
