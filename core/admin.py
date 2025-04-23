from django.contrib import admin
from .models import Film_Post,Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


class FilmPostAdmin(admin.ModelAdmin):
    list_display = ['title','category','created_at']
    search_fields = ['title','category']

admin.site.register(Film_Post,FilmPostAdmin)
admin.site.register(Category,CategoryAdmin)
