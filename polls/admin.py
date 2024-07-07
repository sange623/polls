from django.contrib import admin
from .models import User,PoleTable,PoleHaveOptions,Vote

# Register your models here.
admin.site.register([User,PoleTable,PoleHaveOptions,Vote])