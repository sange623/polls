from django.contrib import admin
from .models import Poll,PoleTable,PoleHaveOptions,Vote

# Register your models here.
admin.site.register([Poll,PoleTable,PoleHaveOptions,Vote])