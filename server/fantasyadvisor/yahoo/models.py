from django.conf import settings
from django.db import models

# Create your models here.


class League(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    game_code = models.CharField(max_length=10, blank=True, default='nfl')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='leagues', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)
