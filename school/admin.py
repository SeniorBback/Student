from django.contrib import admin

from school.models import School,Region,City,District
from acievement.models import GoldenCertificate, Olympiad

admin.site.register(School)
admin.site.register(Region)
admin.site.register(City)
admin.site.register(District)
admin.site.register(GoldenCertificate)
admin.site.register(Olympiad)

# Register your models here.
