from django.db import models

class Subjects(models.Model):
    name = models.CharField(max_length = 11, verbose_name = "Название предмета")


class Themes(models.Model):
    name = models.CharField(max_length = 100, verbose_name = "Название темы")
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='themes', verbose_name="Предмет")


class Tests(models.Model):
    name = models.CharField(max_length = 100, verbose_name = "Название темы")
    theme = models.ForeignKey(Themes, on_delete=models.CASCADE, related_name='tests', verbose_name="Тест")


class Questions(models.Model):
    name = models.CharField(max_length = 100, verbose_name = "Вопрос")
    rightAnswer = models.CharField(max_length = 100, verbose_name = "Правильны(е) ответ(ы)")
    answerOptions = models.CharField(max_length = 300, verbose_name = "Варианты ответов")
    enteringLargeResponce = models.TextField(blank=True, verbose_name="Введите текст...") #Потом перемиеновать, на более подходящее
    enteringSmallResponce = models.CharField(max_length = 100, verbose_name = "Введите текст ...") #Потом перемиеновать, на более подходящее
    test = models.ForeignKey(Tests, on_delete=models.CASCADE, related_name='questions', verbose_name="Вопрос")


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