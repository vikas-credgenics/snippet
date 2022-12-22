from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework import permissions

from common.models import Person
from common.serializers import PersonSerializer


class PersonListV1(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
