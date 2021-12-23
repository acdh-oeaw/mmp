from django.contrib import admin
from topics.models import Topic, ModelingProcess, TextTopicRelation, StopWord


class StopWordAdmin(admin.ModelAdmin):

    search_fields = [
        'word',
    ]


class TopicAdmin(admin.ModelAdmin):
    pass


class ModelingProcessAdmin(admin.ModelAdmin):
    pass


class TextTopicRelationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Topic, TopicAdmin)
admin.site.register(ModelingProcess, ModelingProcessAdmin)
admin.site.register(TextTopicRelation, TextTopicRelationAdmin)
admin.site.register(StopWord, StopWordAdmin)
