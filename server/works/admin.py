from django.contrib import admin
from .models import Team, Work, MediaAsset, Comment, Genre, Tag

# Register your models here.
class MediaAssetInline(admin.TabularInline):
	min_num = 1
	model = MediaAsset

class WorkAdmin(admin.ModelAdmin):
	model = Work
	inlines = [MediaAssetInline]

admin.site.register(Team)
admin.site.register(Work, WorkAdmin)
admin.site.register(MediaAsset)
admin.site.register(Comment)
admin.site.register(Genre)
admin.site.register(Tag)
