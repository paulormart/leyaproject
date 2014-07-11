from django.contrib import admin

from .models import Hello


class HelloAdmin(admin.ModelAdmin):
    pass
admin.site.register(Hello, HelloAdmin)