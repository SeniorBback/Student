from rest_framework import serializers
from personal.models import Subject, Annual, Grade, PersonalFile


class AnnualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annual
        fields = '__all__'


class SubjectlSerializer(serializers.ModelSerializer):
    annual = AnnualSerializer(many=True)
    class Meta:
        model = Subject
        fields = ['id', 'name', 'annual']



class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'


class PersonalFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalFile
        fields = '__all__'