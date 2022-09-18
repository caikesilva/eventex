from django.contrib import admin
from eventex.core.models import Speaker
from django.utils.html import format_html

class SpeakerModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'website_link', 'photo_img']

    def website_link(self, obj):
        return format_html('<a href="{0}">{0}</a>', obj.website)

    website_link.short_description = 'website'

    def photo_img(self, obj):
        return format_html('<img style="border-radius: 100%;" width="32px" src="{}"/>', obj.photo)

    photo_img.short_description = 'Foto'

# Register your models here.
admin.site.register(Speaker, SpeakerModelAdmin)