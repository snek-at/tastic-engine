from django.contrib import admin

from tastic.models import Throughput, BurnDown, Features, Dods, Stories

admin.site.register(Throughput)
admin.site.register(BurnDown)
admin.site.register(Features)
admin.site.register(Dods)
admin.site.register(Stories)
