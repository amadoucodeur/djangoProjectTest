from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, Model3d, Badge 
from django.contrib.auth.models import User

class useProfileInline(admin.StackedInline):
    model = UserProfile

class UserProfileAdmin(UserAdmin):
    inlines = (useProfileInline, )

admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)


class Model3dAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'views')
    list_filter = ('user',)
    search_fields = ('name',)


class BadgeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Model3d, Model3dAdmin)
admin.site.register(Badge, BadgeAdmin)
# Register your models here.
