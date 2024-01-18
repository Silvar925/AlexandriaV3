from django.contrib import admin
from .models import Subjects, Themes, Tests, Questions


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']


@admin.register(Subjects)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

@admin.register(Themes)
class ThemesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

@admin.register(Tests)
class TestsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']
