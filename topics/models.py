from django.db import models


class ModelingProcess(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    process_start = models.DateTimeField()
    process_end = models.DateTimeField()
    modeling_type = models.CharField(max_length=250, default="gensim.models.LdaModel")
    param = models.JSONField()

    def __str__(self):
        return "{self.modeling_type}, created: {self.created_at}"


class Topic(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    word = models.JSONField
    title = models.CharField(max_length=250)
    weight = models.FloatField(blank=True, null=True)
    process = models.ForeignKey(
        'ModelingProcess', on_delete=models.CASCADE
    )
