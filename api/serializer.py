from rest_framework import serializers
from cv.models import CV, Usuario, CvUsuario, Description, \
    PersonalData, Education, WorkExp, Skill, Language, Course, Link


class CVSerialize(serializers.ModelSerializer):
    class Meta:
        model = CV
        fields = ('title', 'language', 'version', 'active')


class UserSerialize(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('username', 'usuario_id')

#
class CvUsuarioSerialize(serializers.ModelSerializer):
    class Meta:
        model = CvUsuario
        fields = ('id', 'cv_id', 'usuario_id', 'personal_data', 'education', 'work_exp', 'skill', 'language',
                  'course', 'link', 'active')

#
class DescriptionSerialize(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = ('id', 'name', 'description')

class PersonalDataSerialize(serializers.ModelSerializer):
    class Meta:
        model = PersonalData
        fields = ('address', 'citi', 'phone','email', 'photo', 'active')


class EducationSerialize(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('title', 'date', 'school', 'finish_date', 'actual', 'finished', 'active')


class WorkExpSerialize(serializers.ModelSerializer):
    class Meta:
        model = WorkExp
        fields = ('title', 'date_start', 'date_finished', 'company', 'city', 'description', 'active')

class SkillSerialize(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('name', 'description')

class LanguageSerialize(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('name', 'level')

class CourseSerialize(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('name', 'description')


class LinkSerialize(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('name', 'url', 'icon', 'active')



