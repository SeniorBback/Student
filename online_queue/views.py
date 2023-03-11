from django.shortcuts import render
from online_queue.serializers import StudentSerializer, StudentPhotoSerializer, NewSerializer, OnlineQueueSerializer, NewPhotoSerializer
from online_queue.models import Student, StudentPhoto, OnlineQueue, NewPhoto, New
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet


class StudentView(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['fullname', 'pin', 'father', 'mother']
    ordering_filters = ['fullname', ]
    filterset_fields = ['fullname', 'grade', 'school', 'father', 'mother']


class StudentPhotoView(ModelViewSet):
    serializer_class = StudentPhotoSerializer
    queryset = StudentPhoto.objects.all()


class NewView(ModelViewSet):
    serializer_class = NewSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title', 'date']
    ordering_filters = ['date', ]
    filterset_fields = ['title', 'text', 'date']
    queryset = New.objects.all()


class NewPhotoView(ModelViewSet):
    serializer_class = NewPhotoSerializer
    queryset = NewPhoto.objects.all()


class OnlineQueueView(ModelViewSet):
    serializer_class = OnlineQueueSerializer
    lookup_field = ''

    def get_queryset(self):
        return self.queryset.get()
