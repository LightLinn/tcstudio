from django.contrib import admin
from blog import models

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    ColumnsName = [
        'Title',
        'Catego',
        'Author',
        'PubTime',
        'Enable',
        'Press',
        'Like',
    ]

    list_display = ColumnsName
    list_filter = ColumnsName
    search_fields = ColumnsName

admin.site.register(models.BlogList, BlogAdmin)