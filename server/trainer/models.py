from django.db import models

# Create your models here.
class Statement(models.Model):
    persona = models.CharField(max_length=200)

    class Meta:
        db_table = 'statements'
        verbose_name = 'Jarvis Dataset'
        verbose_name_plural = 'Jarvis Datasets'