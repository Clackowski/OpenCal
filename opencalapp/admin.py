from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Calendar
    
class CalendarInline(admin.TabularInline):
    model = CustomUser.calendars.through  # Specify the through model for many-to-many relationship
    extra = 1  # Number of empty forms to display
    
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'numCals', 'isFriend')
    inlines = [CalendarInline]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Calendar)