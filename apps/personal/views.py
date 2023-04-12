from apps.personal.serializers import SubjectlSerializer, AnnualSerializer, GradeSerializer

from apps.personal.models import Subject, Annual

from rest_framework.viewsets import ModelViewSet

from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class SubjectView(ModelViewSet):
    serializer_class = SubjectlSerializer
    queryset = Subject.objects.all()

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']
    filterset_fields = ['name']


class AnnualView(ModelViewSet):
    serializer_class = AnnualSerializer
    queryset = Annual.objects.all()

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['subject', 'quarter_1', 'quarter_2', 'quarter_3', 'quarter_4', 'quarter_final']
    ordering_fields = ['subject', 'quarter_1', 'quarter_2', 'quarter_3', 'quarter_4', 'quarter_final']
    filterset_fields = ['subject', 'quarter_1', 'quarter_2', 'quarter_3', 'quarter_4', 'quarter_final']



class GradeView(ModelViewSet):
    serializer_class = GradeSerializer
    queryset = Annual.objects.all()

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['grade']
    ordering_fields = ['grade']
    filterset_fields = ['grade']


class PersonalFileView(ModelViewSet):
    serializer_class = GradeSerializer
    queryset = Annual.objects.all()

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['profile', 'grade']
    ordering_fields = ['profile', 'grade']
    filterset_fields = ['profile', 'grade']



