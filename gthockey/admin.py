from django.contrib import admin

from .models import Player, Game, Team, Rink, Email


class PlayerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


class GameAdmin(admin.ModelAdmin):
    list_display = ['date', 'time', 'opponent']
    fieldsets = [
        ('Date/Time', {'fields': ['date', 'time']}),
        ('Team', {'fields': ['opponent']}),
        ('Location', {'fields': ['venue', 'location']}),
    ]


class TeamAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Team Name', {'fields': ['school_name', 'mascot_name']}),
        ('Other Information', {'fields': ['web_url', 'logo']})
    ]


class RinkAdmin(admin.ModelAdmin):
    pass

admin.site.register(Player, PlayerAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Rink, RinkAdmin)
admin.site.register(Email)
