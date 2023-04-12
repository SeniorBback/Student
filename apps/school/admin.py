from django.contrib import admin

from apps.school.models import School,Region,City,District

admin.site.register(School)
admin.site.register(Region)
admin.site.register(City)
admin.site.register(District)

