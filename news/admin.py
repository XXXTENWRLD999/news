from django.contrib import admin
from .models import News, Category,Commentary
class NewsAdmin(admin.ModelAdmin):
    # list_filter = ["title", "description",'category']
    list_display=["title", "description",'category']

# Register your models here.
admin.site.register(News,NewsAdmin)
admin.site.register(Category)
admin.site.register(Commentary)