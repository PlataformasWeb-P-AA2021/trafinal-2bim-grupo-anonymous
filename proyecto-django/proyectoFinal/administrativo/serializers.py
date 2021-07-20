from django.contrib.auth.models import User, Group
from administrativo.models import Persona, Barrio ,Casa, Departamento

from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Persona
        fields = '__all__'

class BarrioSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Barrio
        fields = '__all__'

class CasaSerializer(serializers.HyperlinkedModelSerializer):
    persona_str = serializers.StringRelatedField(source="personasCasa", read_only=True)
    barrio_str = serializers.StringRelatedField(source="barriosCasa", read_only=True)
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Casa
        fields = '__all__' 

class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    persona_str = serializers.StringRelatedField(source="personasDepa", read_only=True)
    barrio_str = serializers.StringRelatedField(source="barriosDepa", read_only=True)
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Departamento
        fields = '__all__' 