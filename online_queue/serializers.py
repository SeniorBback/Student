from rest_framework import serializers
from .models import Student, StudentPhoto, OnlineQueue, NewPhoto, New


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class StudentPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentPhoto
        fields = '__all__'


class OnlineQueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineQueue
        fields = ['school', 'student', 'sms']



class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = '__all__'


class NewPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewPhoto
        fields = '__all__'
