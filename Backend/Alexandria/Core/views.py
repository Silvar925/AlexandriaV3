from django.shortcuts import render
from rest_framework import generics
from .models import Subjects, Themes, Tests, Questions
from .serializer import SubjectsSerializer, ThemesSerializer, TestsSerializer, QuestionsSerializer


class SubjectsAPIView(generics.ListAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer


class ThemesAPIView(generics.ListAPIView):
    queryset = Themes.objects.all()
    serializer_class = ThemesSerializer

class TestsAPIView(generics.ListAPIView):
    queryset = Tests.objects.all()
    serializer_class = TestsSerializer


class QuestionsAPIView(generics.ListAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer
