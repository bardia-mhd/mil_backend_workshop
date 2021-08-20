from django.contrib import admin

# Register your models here.
from django.utils.html import format_html

from google_keep.models import Note, KeepUser

admin.site.register(Note)

admin.site.site_header = 'مدیریت بکند میل'
admin.site.site_title = 'مدیریت بکند میل'


class KeepUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'is_active', 'email_name')
    list_filter = ('is_active',)
    search_fields = ('email', 'first_name', 'last_name')
    readonly_fields = ('email',)
    exclude = ('is_active',)
    actions = ['change_name']

    def change_name(self, request, queryset):
        for obj in queryset:
            obj.first_name = '+++' + obj.first_name
            obj.save()

    change_name.short_description = '+++ کردن اسم'

    def get_queryset(self, request):
        qs = KeepUser.objects.filter(is_active=True)
        return qs

    def email_name(self, obj: KeepUser):
        return format_html('<h5 style="color:{};text-align:center; border: 2px solid {}">{}</h5>', '#cf2f23', '#cf2f23',
                           obj.email + ' *** ' + obj.first_name)

    email_name.short_description = 'اسم ایمیل'
    email_name.admin_order_field = 'email'


admin.site.register(KeepUser, KeepUserAdmin)
