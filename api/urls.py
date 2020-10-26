from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
        path('cv/', views.CvApi.as_view(), name='cv-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
