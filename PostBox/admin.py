__author__ = 'Antony_Sakkariaz'

from django.contrib import admin
from PostBox.models import Feedback
# The following imports are for modifying the user addition/change view
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class PostMaster(admin.ModelAdmin):
    list_display = ('user', 'date', 'suggestion')
    list_filter = ['date']
    date_hierarchy = 'date'
    fieldsets = [
        (None, {'fields': ['user', 'date', 'sender']}),
        ('Feedback Details', {'fields': [('example', 'consequence'), 'suggestion']}),
    ]

admin.site.register(Feedback, PostMaster)


class MyUserAdmin(UserAdmin):
   fieldsets = [
        (None, {'fields': ['username', 'first_name', 'last_name', 'email']}),
        ('Password', {'fields': ['password']}),
        ('Other Information', {'fields': ['is_superuser', 'is_active', 'is_staff', 'date_joined']}),
    ]

admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
