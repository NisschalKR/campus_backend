from rest_framework import viewsets
from .models import Location, LostItem, FoundItem, JobListing
from .serializers import LocationSerializer, LostItemSerializer, FoundItemSerializer, JobListingSerializer

# Smart Campus Navigation
class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

# Lost & Found
class LostItemViewSet(viewsets.ModelViewSet):
    queryset = LostItem.objects.all()
    serializer_class = LostItemSerializer
    

class FoundItemViewSet(viewsets.ModelViewSet):
    queryset = FoundItem.objects.all()
    serializer_class = FoundItemSerializer

# Career Portal
class JobListingViewSet(viewsets.ModelViewSet):
    queryset = JobListing.objects.all()
    serializer_class = JobListingSerializer
