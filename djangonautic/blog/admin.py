from django.contrib import admin
from .models import blog


class blogAdmin(admin.ModelAdmin):
    list_display = ("title", "body", "author")


admin.site.register(blog, blogAdmin)
