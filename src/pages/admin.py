from django.contrib import admin

from .models import Page, PageSection, PageSlide

# Register your models here.
class PageSectionInline(admin.StackedInline):
    model = PageSection
    extra = 1

class PageSlideInLine(admin.StackedInline):
    model = PageSlide
    extra = 1

class PageAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'parent', 'url', 'created_at', 'updated_at', )
    readonly_fields = ('url', 'created_at', 'updated_at', )
    list_display = ('title', 'url', 'updated_at',)
    prepopulated_fields = {'slug': ('title', )}

    inlines = (PageSlideInLine, PageSectionInline, )


    def save_model(self, request, obj, form, change):
        obj.slug = obj.slug.lower()

        if obj.parent:
            obj.url = obj.parent.url + '/' + obj.slug
        else:
            obj.url = obj.slug

        obj.save()

admin.site.register(Page, PageAdmin)

