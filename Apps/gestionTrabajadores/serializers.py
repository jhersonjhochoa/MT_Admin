from .models import Trabajador
from rest_framework import serializers

class TrabajadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trabajador
        fields = ('dni','apellidos','nombres','fechaNacimiento','foto',)
        read_only_fields  = ('dni','apellidos','nombres','fechaNacimiento','foto',)
