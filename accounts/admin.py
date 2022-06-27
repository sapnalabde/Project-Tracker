from django.contrib import admin
from django.utils.html import format_html
from .models import *


class UserProfileAdmin(admin.ModelAdmin):
    list_display =(
        'user_email', 'username', 'parentuser', 'mobile', 
         'first_name', 'last_name', 'last_login', 'date_joined', 'address',
        'userstatus', 'login_as_user', 'userrole','department')
    list_filter = ('user__date_joined', 'user__last_login', 'userstatus', 'userrole')
    search_fields = ('user__email', 'user__username')

    # def country(self, obj):
    #     if obj.country_detail:
    #         return obj.country_detail.name + "-idd-%s, ccd-+%s" % (obj.country_detail.idd, obj.country_detail.ccd)
    #     else:
    #         return ''

    def login_as_user(self, obj):
        return format_html("<a href=''>login</a>", obj.user.username)

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name

    def last_login(self, obj):
        return obj.user.last_login

    def date_joined(self, obj):
        return obj.user.date_joined

    def user_email(self, obj):
        return obj.user.email

    def username(self, obj):
        return obj.user.username

    '''def get_queryset(self, request):
        qs = super(UserProfileAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(site=request.user.userdetail.site)'''




# class CRMPlusCountAdmin(admin.ModelAdmin):
#     list_display = (
#     'user', 'lead_count', 'contact_count', 'deal_count', 'task_count', 'companies_count', 'added_date', 'modified_date')
#     list_filter = ('added_date',)


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Vertical)

# admin.site.register(CRMPlusCount, CRMPlusCountAdmin)
