from django.contrib import admin

# Register your models here.
from .models import Fixtures, Players, Question, Teams, configdata

admin.site.register(Fixtures)
admin.site.register(Teams)
admin.site.register(configdata)
admin.site.register(Question)
admin.site.register(Players)
