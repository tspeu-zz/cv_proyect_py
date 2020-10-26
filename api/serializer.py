from rest_framework import serializers
from cv.models import CV, Usuario, CvUsuario

class CVSerialize(serializers.ModelSerializer):
    class Meta:
        model = CV
        fields = ('title', 'language', 'version')


class UserSerialize(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('username', 'usuario_id')

class CvUsuarioSerialize(serializers.ModelSerializer):
    class Meta:
        model = CvUsuario
        fields = ('id', 'cv_id', 'usuario_id')
