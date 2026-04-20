from django.urls import path
from .views import test_scraper
from .views import list_posts

urlpatterns = [
    path('test/', test_scraper),
    path('posts/', list_posts),
]
