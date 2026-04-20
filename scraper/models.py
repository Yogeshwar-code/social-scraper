from django.db import models

# Create your models here.
class ScrapedPost(models.Model):
    
   # This model stores each scraped social media post
    
    # Platform name: Twitter, Instagram, Facebook etc.
    platform = models.CharField(
        max_length=50,
        help_text="Social media platform name (Twitter, Instagram, etc.)"
    )

    # Username or page name (Username is same as author)
    username = models.CharField(
        max_length=150,
        help_text="Username of the account"
    )

    # Main post content (content is same as post_text)
    post_text = models.TextField(
        help_text="Content of the post"
    )

    # Original post URL
    post_url = models.URLField(
        max_length=500,
        unique=True,
        help_text="Direct URL of the post"
    )
    
    # Engagement data
    likes_count = models.PositiveIntegerField(
        default=0,
        help_text="Number of likes"
    )

    comments_count = models.PositiveIntegerField(
        default=0,
        help_text="Number of comments"
    )

    # When the post was created on social media
    #post_created_at = models.DateTimeField(null=True, blank=True)

    # When we scraped it
    scraped_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Time when the post was scraped"
    )
    
    def __str__(self):
        return f"{self.platform} | {self.username}"