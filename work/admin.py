from django.contrib import admin
from work.models import Category, Sample


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('label',)}

class SampleAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'status', 'created', 'modified')
    search_fields = ('title', 'content')
    list_filter = ('status', 'owner', 'created', 'modified')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Sample, SampleAdmin)
