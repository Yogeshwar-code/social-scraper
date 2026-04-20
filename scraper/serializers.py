from rest_framework import serializers
from .models import ScrapedPost


class ScrapedPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapedPost
        fields = '__all__'