from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
# admin.site.register(RaingouProject)
# admin.site.register(RaingouSkill)


@admin.register(RaingouProject)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'description', 'techonolies_use')
    search_fields = ('title', 'description')
    list_filter = ('title',  'user')

@admin.register(RaingouSkill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'user')
    search_fields = ('name', 'category')
    list_filter = ('name',  'user')

admin.site.site_header = "Portfolio Administration"
admin.site.site_title = "Portfolio Admin Portal"
admin.site.index_title = "Welcome to Portfolio Administration"


