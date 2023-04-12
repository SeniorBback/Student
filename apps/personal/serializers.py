from rest_framework import serializers
from .models import Annual, Grade, PersonalFile



class AnnualSerializer(serializers.ModelSerializer):

    class Meta:
        model = Annual
        fields = '__all__'


class GradeSerializer(serializers.ModelSerializer):
    annual = AnnualSerializer(many=True)

    class Meta:
        model = Grade
        fields = '__all__'


class PersonalFileSerializer(serializers.ModelSerializer):
    class_info = GradeSerializer(many=True)

    class Meta:
        model = PersonalFile
        fields = '__all__'