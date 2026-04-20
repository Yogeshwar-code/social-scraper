from django.contrib import admin

# Register your models here. it is responsible for how admin panel looks on webpages 
# or how the logging structure looks or cantain tables in webpage

from .models import ScrapedPost

@admin.register(ScrapedPost)
class ScrapedPostAdmin(admin.ModelAdmin):
    list_display = ("platform", "username", "likes_count", "comments_count", "scraped_at")
    search_fields = ("platform", "username")
    list_filter = ("platform", "scraped_at")