from django.urls import path
from . import views

urlpatternsCore = [
    path('subjectList/', views.SubjectsAPIView.as_view(), name='subjectList'),
    path('themesList/', views.ThemesAPIView.as_view(), name='themesList'),
    path('testsList/', views.TestsAPIView.as_view(), name='testsList'),
    path('questionsList/', views.QuestionsAPIView.as_view(), name='questionsList'),
]