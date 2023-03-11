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


    class Meta:
        model = School
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        print(response)
        # response['similar_count'] = len(response['likes'])-len(response['dislikes'])
        return response



