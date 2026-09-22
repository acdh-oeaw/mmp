from django.contrib import admin
from .models import *
from reversion.admin import VersionAdmin
from mptt.admin import MPTTModelAdmin


# With object permissions support
@admin.register(SkosConcept)
class SkosConceptAdmin(MPTTModelAdmin, VersionAdmin):
	pass


class SkosCollectionAdmin(VersionAdmin):
	pass


class SkosConceptSchemeAdmin(VersionAdmin):
	pass


admin.site.register(SkosCollection, SkosCollectionAdmin)
admin.site.register(SkosConceptScheme, SkosConceptSchemeAdmin)
admin.site.register(ConceptSchemeTitle)
admin.site.register(ConceptSchemeDescription)
admin.site.register(ConceptSchemeSource)
admin.site.register(CollectionLabel)
admin.site.register(CollectionNote)
admin.site.register(CollectionSource)
admin.site.register(ConceptLabel)
admin.site.register(ConceptNote)
admin.site.register(ConceptSource)
