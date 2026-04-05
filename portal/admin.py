from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Profile, Resource, Category


class ProfileAdmin(ImportExportModelAdmin):
    pass


class ResourceAdmin(ImportExportModelAdmin):
    pass


class CategoryAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(Category, CategoryAdmin)