from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import School
from .serializers import SchoolSerializer



class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    search_fields = ['fullname']
    filterset_fields = ['district','region','city']

    # ordering_fields = ['rating_count']



