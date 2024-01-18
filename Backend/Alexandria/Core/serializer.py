from rest_framework import serializers
from .models import Subjects, Themes, Tests, Questions

class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = '__all__'


class ThemesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Themes
        fields = '__all__'


class TestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tests
        fields = '__all__'


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'
