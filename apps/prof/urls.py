from django.urls import path
from apps.prof.views import ProfileViewSet


urlpatterns = [
    path('', ProfileViewSet.as_view({'get':'list'})),
    path('<int:pk>', ProfileViewSet.as_view({'get':'retrieve'})),
]