from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Calendar, Event
    
class EventInline(admin.TabularInline):
    model = Event
    extra = 1
    
class CalendarAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'last_modified']
    inlines = [EventInline]
    
class CalendarInline(admin.TabularInline):
    model = CustomUser.calendars.through  # Specify the through model for many-to-many relationship
    extra = 1  # Number of empty forms to display
    
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'numCals')
    inlines = [CalendarInline]
    
class CustomUserInline(admin.TabularInline):
    model = Calendar.contributors.through
    extra = 1
    


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Calendar, CalendarAdmin)
admin.site.register(Event)