from django.contrib import admin
from contentmanage import models

# Register your models here.

class ContentAdmin(admin.ModelAdmin):
    ColumnsName = [
        'BlockName',
        'Title',
        'CreateDate',
    ]

    list_display = ColumnsName
    list_filter = ColumnsName
    search_fields = ColumnsName

class TDKAdmin(admin.ModelAdmin):
    ColumnsName = [
        'Title',
        'Description',
        'Keywords',
    ]

    list_display = ColumnsName
    list_filter = ColumnsName
    search_fields = ColumnsName

admin.site.register(models.ContentList, ContentAdmin)
admin.site.register(models.TDKList, TDKAdmin)