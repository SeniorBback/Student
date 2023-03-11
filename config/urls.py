from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('online_queue/', include('online_queue.urls')),
    path('school',include('school.urls')),
] 
