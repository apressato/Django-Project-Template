from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ExtendedUser, Roles


@admin.register(ExtendedUser)
class CustomAdmin(UserAdmin):
    list_display = ['email', 'first_name', 'last_name']
    fieldsets = (
        (None, {"fields": ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'profile_image', 'image_tag', 'UseGravatar',
                                      'Short_Intro',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'roles', 'groups', 'user_permissions')}),
        ('Social Media', {'fields': ('Social_LinkedIn', 'Social_Instagram', 'Social_facebook')}),
        ('Extra fields', {'fields': ('CultureId', 'Screen_scale')})
    )
    readonly_fields = ['image_tag']
    ordering = ('email',)


admin.site.register(Roles)

