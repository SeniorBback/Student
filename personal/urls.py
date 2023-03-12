from django.urls import path
from personal.views import SubjectView

urlpatterns = [
    path('subject', SubjectView.as_view({'get': 'list'})),
    path('annual', SubjectView.as_view({'get': 'list'})),
    path('grade', SubjectView.as_view({'get':'list'})),
    path('personalfile', SubjectView.as_view({'get': 'list'}))
]