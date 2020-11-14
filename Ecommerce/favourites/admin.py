from django.contrib import admin
from .models import Favourite


class FavAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'date_added')
    search_fields = ('user', 'item')


admin.site.register(Favourite, FavAdmin)
