from rest_framework import serializers
from .models import School
from acievement.models import GoldenCertificate, Olympiad
from online_queue.serializers import OnlineQueueSerializer


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
    queue = OnlineQueueSerializer(many=True)


    class Meta:
        model = School
        fields = '__all__'
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        print(response)
        response['free_spots'] = response['spots']-len(response['queue'])
        return response



