from django.contrib import admin
from .models import Message, AboutUs, Classes, Schedules

admin.site.register(Message)
admin.site.register(AboutUs)
admin.site.register(Classes)
admin.site.register(Schedules)
