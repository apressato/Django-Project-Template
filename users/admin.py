from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ExtendedUser, Roles


@admin.register(ExtendedUser)
class CustomAdmin(UserAdmin):
    list_display = ['username', 'first_name', 'last_name']
    fieldsets = UserAdmin.fieldsets + (('Extra fields', {'fields': ('profile_image', 'image_tag', 'UseGravatar',
                                                                    'roles',
                                                                    'Short_Intro', 'Social_LinkedIn', 'Social_Instagram',
                                                                    'Social_facebook', 'CultureId', 'Screen_scale',)}),)
    readonly_fields = ['image_tag']


admin.site.register(Roles)

