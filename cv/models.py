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


# description
class Description(models.Model):
    name = models.CharField(max_length=60, null=True)
    description = models.CharField(max_length=4000, null=True)

    def __str__(self):
        return f'{self.name}, {self.description} '


#   detalles
class PersonalData(models.Model):
    title = models.CharField(max_length=60, null=True)
    name = models.CharField(max_length=60, null=True)
    address = models.CharField(max_length=50, null=True)
    citi = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=50, null=True)
    photo = models.CharField(max_length=50, null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return f'{self.title}, {self.name}, {self.address}, {self.citi}, {self.phone}, {self.email}, {self.photo}, {self.active}'
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

    def __str__(self):
        return f'{self.title}, {self.date}, {self.school} , {self.finish_date} , {self.actual}, {self.finished}, {self.active}'

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

    def __str__(self):
        return f'{self.title}, {self.date_start}, {self.date_finished} , {self.company} , {self.city}, {self.created}, {self.description}, {self.active}'


#
class Skill(models.Model):
    name = models.CharField(max_length=60, null=True)
    description = models.ManyToManyField(Description, help_text="escoger una description")

    def __str__(self):
        return f'{self.name}, {self.description}'

class Language(models.Model):
    name = models.CharField(max_length=20, null=True)
    level = models.CharField(max_length=15, null=True)

    def __str__(self):
        return f'{self.name}, {self.level}'

class Course(models.Model):
    name = models.CharField( max_length=60, null=True)
    description = models.CharField(max_length=60, null=True)

    def __str__(self):
        return f'{self.name}, {self.description}'

class Link(models.Model):
    name = models.CharField( max_length=20, null=True)
    url = models.CharField(max_length=80, null=True)
    icon = models.CharField(max_length=30, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}, {self.url}, {self.icon}, {self.active}'


#
class CvUsuario(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=0)
    cv = models.OneToOneField(CV, on_delete=models.SET_DEFAULT, default=0)
    personal_data = models.OneToOneField(PersonalData, on_delete=models.SET_DEFAULT, default=0)
    education = models.ManyToManyField(Education,  help_text="escoger una educacion...")
    work_exp = models.ManyToManyField(WorkExp,  help_text="escoger una experiencia...")
    skill = models.ManyToManyField(Skill,  help_text="escoger una skill...")
    language = models.ManyToManyField(Language,  help_text="escoger un lenguaje ...")
    course = models.ManyToManyField(Course,  help_text="escoger un curso ...")
    link = models.ManyToManyField(Link,  help_text="escoger un link ...")
    # active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    #
    def __str__(self):
        return f'{self.usuario.__str__()}, {self.cv.__str__()} {self.personal_data}, {self.education}, ' \
               f'{self.work_exp}, {self.skill}, {self.language}, {self.course},  {self.link}'




