from django.urls import path
from online_queue.views import StudentView, NewView, OnlineQueueView

urlpatterns = [
    path('', StudentView.as_view({'get': 'list'})),
    path('<int:pk>', StudentView.as_view({'get': 'retrieve'})),
    path('news', NewView.as_view({'get': 'list'})),
    path('queue', OnlineQueueView.as_view({'get': 'list', 'post': 'create'})),
    path('queue/<int:pk>', OnlineQueueView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
