from django.contrib import admin
from .models import *


class ArtifactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'stats', 'history', 'time_create', 'time_update', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published', )


class SetsAdmin(admin.ModelAdmin):
    list_display = ('id', 'set_name', 'bonus')
    list_display_links = ('id', 'set_name')
    search_fields = ('set_name', 'bonus')


admin.site.register(Artifacts, ArtifactsAdmin)
admin.site.register(Sets, SetsAdmin)