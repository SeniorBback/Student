from django.shortcuts import render
from online_queue.serializers import StudentSerializer, StudentPhotoSerializer, NewSerializer, OnlineQueueSerializer, NewPhotoSerializer
from online_queue.models import Student, StudentPhoto, OnlineQueue, NewPhoto, New
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status, response


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
    queryset = OnlineQueue.objects.all()
    # lookup_field = 'on_pk'
    #
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save(
    #         school=kwargs.get('on_pk')
    #     )
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED,
    #                     headers=headers)
    #
    # def get_queryset(self):
    #     return self.queryset.get()
