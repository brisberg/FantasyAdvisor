from django.db import models

# Create your models here.


class League(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    game_code = models.CharField(max_length=10, blank=True, default='nfl')

    class Meta:
        ordering = ('created',)
