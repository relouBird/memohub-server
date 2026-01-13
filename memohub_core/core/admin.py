from django.contrib import admin

# Register your models here.
from .models import Track, Supervisor, KeyWord, Memories, StatisticsConsultation

admin.site.register(Track)
admin.site.register(Supervisor)
admin.site.register(KeyWord)
admin.site.register(Memories)
admin.site.register(StatisticsConsultation)