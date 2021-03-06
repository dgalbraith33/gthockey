from django.contrib import admin
from django import forms

from .models import Player, Game, Team, Rink, Email, NewsStory, Season, Board, Coach, ShopItem, \
    ShopItemOptionList, ShopItemImage, ShopItemCustomOption


class PlayerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


class GameAdmin(admin.ModelAdmin):
    list_display = ['date', 'time', 'opponent', 'season']
    list_filter = ['season']
    fieldsets = [
        ('Date/Time', {'fields': ['date', 'time', 'season']}),
        ('Team', {'fields': ['opponent']}),
        ('Location', {'fields': ['venue', 'location']}),
        ('Time', {'fields': ['period', 'minutes', 'seconds']}),
        ('Score GT', {'fields': ['score_gt_first', 'score_gt_second', 'score_gt_third',
                                 'score_gt_ot', 'score_gt_final']}),
        ('Score Opp', {'fields': ['score_opp_first', 'score_opp_second', 'score_opp_third',
                                  'score_opp_ot', 'score_opp_final']})
    ]


class TeamAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Team Name', {'fields': ['school_name', 'mascot_name']}),
        ('Other Information', {'fields': ['web_url', 'logo']})
    ]


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title']

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(NewsAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'content':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield


class RinkAdmin(admin.ModelAdmin):
    pass


class BoardAdmin(admin.ModelAdmin):
    list_display = ['position', 'last_name']

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(BoardAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'description':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield


class CoachAdmin(admin.ModelAdmin):
    list_display = ['coach_position', 'last_name']

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(CoachAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'description':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield


class ShopItemOptionListInline(admin.StackedInline):
    model = ShopItemOptionList
    extra = 1


class ShopItemCustomOptionInline(admin.StackedInline):
    model = ShopItemCustomOption
    extra = 1


class ShopItemImageInline(admin.StackedInline):
    model = ShopItemImage
    extra = 1


class ShopItemAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [
        ShopItemOptionListInline,
        ShopItemCustomOptionInline,
        ShopItemImageInline,
    ]

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(ShopItemAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'description':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield


admin.site.register(Player, PlayerAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(NewsStory, NewsAdmin)
admin.site.register(Rink, RinkAdmin)
admin.site.register(Email)
admin.site.register(Season)
admin.site.register(Board, BoardAdmin)
admin.site.register(Coach, CoachAdmin)
admin.site.register(ShopItem, ShopItemAdmin)
