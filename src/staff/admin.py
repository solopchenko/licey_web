from django.contrib import admin

from .models import Person, PersonPosition, PersonTab
# Register your models here.

class PersonTabInline(admin.TabularInline):
    model = PersonTab
    extra = 0

class PersonAdmin(admin.ModelAdmin):
    fields = ('user', 'last_name', 'first_name', 'middle_name', 'office', 'positions', 'education', 'teaching_experience', 'photo', 'email', 'phone', )
    inlines = (PersonTabInline, )

admin.site.register(Person, PersonAdmin)
admin.site.register(PersonPosition)
