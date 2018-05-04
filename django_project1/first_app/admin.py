from django.contrib import admin

# Register your models here.

from first_app.models import Topic, Webpage, AccessRecodrd

admin.site.register(AccessRecodrd)
admin.site.register(Webpage)
admin.site.register(Topic)
