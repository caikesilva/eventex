from urllib import request
from django.contrib import admin
from eventex.core.models import Course, Speaker, Contact, Talk
from django.utils.html import format_html

class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1

class SpeakerModelAdmin(admin.ModelAdmin):
    inlines = [ContactInline]
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'photo_img', 'website_link', 'email', 'phone']

    def website_link(self, obj):
        return format_html('<a href="{0}">{0}</a>', obj.website)

    website_link.short_description = 'website'

    def photo_img(self, obj):
        return format_html('<img style="border-radius: 100%;" width="32px" src="{}"/>', obj.photo)

    photo_img.short_description = 'Foto'

    def email(self, obj):
        return obj.contact_set.emails().first()
    
    email.short_description = 'Email'

    def phone(self, obj):
        return obj.contact_set.phones().first()

    phone.short_description = 'Telefone'

class TalkModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.filter(course=None)
        return queryset

# Register your models here.
admin.site.register(Speaker, SpeakerModelAdmin)
admin.site.register(Talk, TalkModelAdmin)
admin.site.register(Course)