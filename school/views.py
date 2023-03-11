from django.db.models import Count
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import School
from .serializers import SchoolSerializer



class SchoolViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    search_fields = ['fullname']
    filterset_fields = ['district','region','city']

    ordering_fields = ['rating']

    def get_queryset(self):
        # percent_1 = int(len(response['olympiad']) * 100 / 30)
        return School.objects.all().annotate(rating=
                                             ((Count('golden__points') * 100 / 30) + (Count('olympiad__place') * 100 / 50)),
                                            )



