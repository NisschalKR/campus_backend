from rest_framework import serializers
from .models import Location, LostItem, FoundItem, JobListing

# Smart Campus Navigation
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

# Lost & Found
class LostItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostItem
        fields = '__all__'
    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None

class FoundItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoundItem
        fields = '__all__'

# Career Portal
class JobListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobListing
        fields = '__all__'
