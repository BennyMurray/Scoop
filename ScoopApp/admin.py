from django.contrib import admin
from .models import CraftBeer
from .models import Test
from django.utils.html import format_html



class CraftBeerAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" width="100" />'.format(obj.image_link))

    image_tag.short_description = 'Image'

    list_display = ['beer_name', 'beerID', 'ABV', 'IBU', 'SRM', 'acidity', 'sequence_added', 'image_tag', ]

admin.site.register(CraftBeer, CraftBeerAdmin)

admin.site.register(Test)
