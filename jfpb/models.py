from django.db import models
class Login(models.Model):
    usuario = models.CharField(max_length=10)
    senha = models.CharField(max_length=10)
# Create your models here.
class Heroe(models.Model):
    class Meta:
        verbose_name = 'heroe'
class Villain(models.Model):
    class Meta:
        verbose_name = 'Villain'

class Author(models.Model):
    class Meta:
        verbose_name = 'Author'

class Joinha(models.Model):
    class Meta:
        verbose_name = 'Joinha'

