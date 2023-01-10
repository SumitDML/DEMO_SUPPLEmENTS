from rest_framework import serializers
from .models import *


class ZoneSerializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()

    class Meta:
        model = Zones
        fields = "__all__"


class SunshineAvailabilitySerializer(serializers.HyperlinkedModelSerializer):
    emp_id = serializers.ReadOnlyField()

    class Meta:
        model = SunshineAvailability
        fields = "__all__"
