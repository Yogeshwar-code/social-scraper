from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ScrapedPost
from .serializers import ScrapedPostSerializer


@api_view(["GET"])
def test_scraper(request):
    """
    Temporary test API to insert dummy data
    """

    post, created = ScrapedPost.objects.get_or_create(
        post_url="https://twitter.com/test/123",
        defaults={
            "platform": "Twitter",
            "username": "test_user",
            "post_text": "This is a test scraped post",
            "likes_count": 10,
            "comments_count": 2,
        },
    )

    return Response(
        {
            "created": created,
            # "message": "Test post created successfully",
            "post_id": post.id,
        }
    )


@api_view(["GET"])
def list_posts(request):
    posts = ScrapedPost.objects.all()
    serializer = ScrapedPostSerializer(posts, many=True)
    return Response(serializer.data)


"""
 post = ScrapedPost.objects.create(
        platform="Twitter",
        username="test_user",
        post_text="This is a test scraped post",
        post_url="https://twitter.com/test/123",
        likes_count=10,
        comments_count=2
    )
"""
