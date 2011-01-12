from django.contrib import admin

from models import Player


class PlayerAdmin(admin.ModelAdmin):
    list_filter   = ('bnetnick', 'updated_at')
    ordering      = ('-created_at',)
    list_display  = ('bnetnick', 'author', 'created_at', 'is_removed')
    search_fields = ('bnetnick',)
admin.site.register(Player, PlayerAdmin)
