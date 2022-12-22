from rest_framework import serializers

from common.models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
