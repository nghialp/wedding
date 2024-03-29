from django.contrib import admin
from .models import *

# import django.contrib.auth.models
# from django.contrib import auth

# admin.site.unregister(auth.models.Group)

# Register your models here.
admin.site.site_header = "Wedding"
admin.site.site_title = "Quản Lý Admin"
admin.site.index_title = "Quản Lý Admin"
admin.site.login_template = "admin/login_template.html"
admin.site.index_template = "admin/index.html"


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    # readonly_fields = ('image_tag',)
    list_display = ('id', 'name', 'slug', 'father', 'mother', 'address', 'child_index', 'ishusban', 'image_tag', 'short_content', 'code', 'user')
    fields = ('name', 'father', 'mother', 'address', 'child_index', 'ishusban','image', 'code', 'decription')
    ordering = ('id', 'name',)
    search_fields = ('name', 'code', 'name', 'slug', 'father', 'mother', 'address', 'decription')
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

# admin.site.register(About)
# admin.site.register(Wedding_Invitation)
@admin.register(Wedding_Invitation)
class Wedding_InvitationAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'location','short_content', 'feast', 'time_calendar', 'time_lunar')
    fields = ('code', 'location', 'gmap', 'feast', 'time_calendar', 'time_lunar')
    ordering = ('id', 'code', 'location', 'feast', 'time_calendar', 'time_lunar')
    search_fields = ('code___name', 'location', 'feast', 'time_calendar', 'time_lunar')
    
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'gallery', 'path_img', 'slide_show', 'decription')
    fields = ('gallery', 'path_img', 'slide_show', 'decription' )
    ordering = ('id', 'gallery', 'path_img', 'slide_show', 'decription')
    search_fields = ('gallery__title', 'decription')
    list_per_page = 15

# class ImageInline(admin.TabularInline):
#     model = Image

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    fields = ('title', 'decription' )
    ordering = ('id', 'title',)
    search_fields = ('title',)
    list_per_page = 15
# admin.site.register(Gallery)
# admin.site.register(Image)

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    fields = ('title', 'images', 'content', 'feeling' )
    # readonl = ('image_tag',)
    list_display = ('id', 'title', 'uploaded_at', 'image_tag', 'feeling', 'user')
    ordering = ('title',)
    search_fields = ('title',)
    list_per_page = 15
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
# admin.site.register(Story)
# admin.site.register(Invitee)
@admin.register(Invitee)
class InviteeAdmin(admin.ModelAdmin):
    fields = ('name', 'wedding', 'phone', 'address','guestof', 'ivitation', 'adherence_wedding', 'money_wedding')
    list_display = ('id', 'name','wedding', 'phone', 'address','guestof', 'ivitation', 'adherence_wedding', 'money_wedding', 'user')
    ordering = ('id', 'name','guestof', 'wedding', 'ivitation', 'adherence_wedding')
    search_fields = ('name', 'wedding', 'phone', 'address', 'guestof', 'ivitation', 'adherence_wedding', 'money_wedding')
    list_per_page = 15
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link', 'image_tag', 'uploaded_at', 'user')
    fields = ('id', 'name', 'link', 'background')
    readonly_fields = ('image_tag',)
    ordering = ('name','link', 'user')
    search_fields = ('name',)
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'short_link', 'menu', 'play_show', 'uploaded_at', 'user')
    fields = ('name', 'link', 'play_show', 'menu')
    # readonly_fields = ('image_tag',)
    ordering = ('id', 'name', 'user')
    search_fields = ('name', 'slug', 'menu__name')
    list_per_page = 15
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

@admin.register(Blessing)
class BlessingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'relation', 'blessing')
    readonly_fields = ('name', 'relation', 'blessing')
    ordering = ('id', 'name', 'relation', 'blessing')
    search_fields = ('name','relation', 'blessing')
    list_per_page = 15
# admin.site.register(Blessing)

