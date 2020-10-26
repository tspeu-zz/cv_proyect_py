from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from cv.models import CV, Usuario, CvUsuario
from .serializer import CVSerialize, CvUsuario, CvUsuarioSerialize


# Create your views here.
class CvApi(APIView):
    """
    List all surveys, or create a new survey
    """
    # @staticmethod
    def get(self, request, format=None):
        _cv = CV.objects.all()
        _serilize = CVSerialize(_cv, many=True)
        return Response(_serilize.data)

    # @staticmethod
    def post(self, request, format=None):
        serializer = CVSerialize(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

