from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from cv.models import CV, Usuario, CvUsuario, PersonalData, Education, WorkExp, Skill, Language, Course, Link



# Register your models here.

admin.site.register(CV)
admin.site.register(Usuario, UserAdmin)
admin.site.register(CvUsuario)
admin.site.register(PersonalData)
admin.site.register(Education)
admin.site.register(WorkExp)
admin.site.register(Skill)
admin.site.register(Language)
admin.site.register(Course)
admin.site.register(Link)
