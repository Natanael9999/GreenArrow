from django.contrib import admin

# Register your models here.

from .models import Heroes
from .models import Villain
from .models import Places

admin.site.register(Heroes)
admin.site.register(Villain)
admin.site.register(Places)