from django.contrib import admin
from topics.models import Topic, ModelingProcess


class TopicAdmin(admin.ModelAdmin):
    pass


class ModelingProcessAdmin(admin.ModelAdmin):
    pass


admin.site.register(Topic, TopicAdmin)
admin.site.register(ModelingProcess, ModelingProcessAdmin)
