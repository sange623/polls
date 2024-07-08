from django.contrib import admin
from .models import Poll,PollTable,PollHaveOptions,Vote

# Register your models here.
admin.site.register([Poll,PollTable,PollHaveOptions,Vote])