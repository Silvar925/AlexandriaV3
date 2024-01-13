from django.contrib import admin
from .models import Subjects, Themes, Tests, Questions

@admin.register(Subjects)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ('name')
    search_fields = ['name']


@admin.register(Themes)
class ThemesAdmin()