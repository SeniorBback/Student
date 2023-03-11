from rest_framework import serializers
from .models import School
from acievement.models import GoldenCertificate, Olympiad


class GoldenCertificateSerializer(serializers.ModelSerializer):

    class Meta:
        model = GoldenCertificate
        fields = '__all__'


class OlympiadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Olympiad
        fields = '__all__'


class SchoolSerializer(serializers.ModelSerializer):
    golden = GoldenCertificateSerializer(many=True)
    olympiad = OlympiadSerializer(many=True)
    rating = serializers.IntegerField()


    class Meta:
        model = School
        fields = '__all__'



