from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from profiles.models import Profile, Service, ServiceConfiguration


class ServiceAdmin(admin.ModelAdmin):
    model = Service


class ServiceConfigurationInline(admin.StackedInline):
    model = ServiceConfiguration


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(UserAdmin):
    inlines = (
        ProfileInline,
        #ServiceConfigurationInline
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Service, ServiceAdmin)
