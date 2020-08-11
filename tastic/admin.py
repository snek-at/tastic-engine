from django.contrib import admin

from tastic.models import Throughput, BurnDown

admin.site.register(Throughput)
admin.site.register(BurnDown)
