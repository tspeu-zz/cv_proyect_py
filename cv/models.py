from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


# Create your models here.
class CV(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    language = models.CharField(max_length=2)
    version = models.CharField(max_length=11)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return f' {self.title}, {self.language}, {self.version}'


class Usuario(AbstractUser):
    usuario_id = models.AutoField(primary_key=True)

    def __str__(self):
        return f'{self.username}, {self.email} {self.usuario_id}'


class CvUsuario(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=0)
    cv = models.OneToOneField(CV, on_delete=models.SET_DEFAULT, default=0)
    peronal_data = models.
    def __str__(self):
        return f'{self.usuario.__str__()}, {self.cv.__str__()} '


# description
class Description(models.Model):
    name = models.CharField(max_length=60, null=True)
    description = models.CharField(max_length=4000, null=True)


#   detalles
class PersonalData(models.Model):
    address = models.CharField(max_length=50, null=True)
    citi = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=50, null=True)
    photo = models.CharField(max_length=50, null=True)
    active = models.BooleanField(default=True )
    created = models.DateTimeField(auto_now_add=True, auto_now=False)


#
class Education(models.Model):
    title = models.CharField(max_length=60, null=True)
    date = models.CharField(max_length=10, null=True)
    school = models.CharField(max_length=20, null=True)
    finish_date = models.CharField(max_length=10, null=True)
    actual = models.BooleanField(default=False)
    finished = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

#
class WorkExp(models.Model):
    title = models.CharField(max_length=60, null=True)
    date_start = models.CharField(max_length=10, null=True)
    date_finished = models.CharField(max_length=10, null=True)
    company = models.CharField(max_length=60, null=True)
    city = models.CharField(max_length=10, null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    description = models.ManyToManyField(Description, help_text="escoger una description")

#
class Skill(models.Model):
    name = models.CharField(max_length=60, null=True)
    description = models.ManyToManyField(Description, help_text="escoger una description")

class Language(models.Model):
    name = models.CharField(max_length=20, null=True)
    level = models.CharField(max_length=15, null=True)

class Course(models.Model):
    name = models.CharField( max_length=60, null=True)
    description = models.CharField(max_length=60, null=True)

class Link(models.Model):
    name = models.CharField( max_length=20, null=True)
    url = models.CharField(max_length=80, null=True)
    icon = models.CharField(max_length=30, null=True)






