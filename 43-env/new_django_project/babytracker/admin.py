from django.contrib import admin
from babytracker.models import BabyInfo, GrowthRecord

admin.site.register(BabyInfo)
admin.site.register(GrowthRecord)
