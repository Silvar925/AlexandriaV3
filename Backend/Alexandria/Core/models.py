from django.db import models
from UserProfile.models import UserAlexandria

class Subjects(models.Model):
    name = models.CharField(max_length = 11, verbose_name = "Название предмета")

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"

    def __str__(self):
        return self.name


class Themes(models.Model):
    name = models.CharField(max_length = 100, verbose_name = "Название темы", default='default_value')
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='themes', verbose_name="Предмет")

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"

    def __str__(self):
        return self.name


class Tests(models.Model):
    name = models.CharField(max_length = 100, verbose_name = "Название темы", default='default_value')
    partition = models.CharField(max_length = 100, verbose_name = "Раздел", null=True, blank=True)
    schoolClass = models.IntegerField(default=0)
    complexity = models.CharField(max_length=100, verbose_name="Уровень сложности", null=True, blank=True)
    theme = models.ForeignKey(Themes, on_delete=models.CASCADE, related_name='tests', verbose_name="Тест")

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"

    def __str__(self):
        return self.name


class Questions(models.Model):
    name = models.CharField(max_length = 500, verbose_name = "Вопрос", default='default_value')
    rightAnswer = models.CharField(max_length = 100, verbose_name = "Правильны(е) ответ(ы)")
    answerOptions = models.CharField(max_length = 300, verbose_name = "Варианты ответов")
    enteringLargeResponce = models.TextField(blank=True, verbose_name="Введите текст...") 
    enteringSmallResponce = models.CharField(max_length = 100, verbose_name = "Введите текст ...", blank = True) 
    test = models.ForeignKey(Tests, on_delete=models.CASCADE, related_name='questions', verbose_name="Тест")

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.name


# class answersTests(models.Model):
#     timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время отправки ответа")
#     score = models.PositiveIntegerField(verbose_name="Баллы за тест")
    
#     STATUS_CHOICES = [
#         ('completed', 'Завершено'),
#         ('not_completed', 'Не завершено'),
#     ]

#     status = models.CharField(
#         max_length=20,
#         choices=STATUS_CHOICES,
#         default='not_completed',
#         verbose_name="Статус"
#     )