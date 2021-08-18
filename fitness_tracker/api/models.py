from django.contrib.auth.models import User
from django.db import models

ACTIVITY_TYPES = (
    ('walking', 'Ходьба'),
    ('running', 'Бег'),
    ('cycling', 'Велосипед'),
)


class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    start_of_activity = models.DateTimeField(verbose_name='Начало активности')
    end_of_activity = models.DateTimeField(verbose_name='Конец активности')
    type_active = models.CharField(max_length=8, verbose_name='Тип активности', choices=ACTIVITY_TYPES, )
    distance = models.FloatField(verbose_name='Дистанция в метрах')
    calorie_count = models.FloatField(verbose_name='Количество калорий')

    def __str__(self):
        return f'{self.user}'