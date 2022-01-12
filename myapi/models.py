from django.db import models

class Merop(models.Model):
    name = models.CharField('Название мероприятия ', max_length=200)
    participants = models.CharField('Количество участников', max_length=200)
    date = models.CharField('Дата', max_length=200)
    place = models.CharField('Место', max_length=200)
    description = models.TextField('Описание', max_length=3000)

    def __str__(self):
        return self.name