from django.contrib import admin
from .models import Activity


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'daily_time', 'weekly_time')


admin.site.register(Activity, ActivityAdmin)
