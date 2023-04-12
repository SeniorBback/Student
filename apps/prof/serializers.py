from rest_framework import serializers
from .models import Profile, HistoryOfStudy, Achievement

from apps.personal.serializers import PersonalFileSerializer


class AchievementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Achievement
        fields = '__all__'


class HistoryOfStudySerializer(serializers.ModelSerializer):

    class Meta:
        model = HistoryOfStudy
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    personal = PersonalFileSerializer(many=True)
    achievement = AchievementSerializer(many=True)
    history = HistoryOfStudySerializer(many=True)

    class Meta:
        model = Profile
        fields = '__all__'