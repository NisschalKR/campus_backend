from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LocationViewSet, LostItemViewSet, FoundItemViewSet, JobListingViewSet
from django.conf.urls.static import static
from django.conf import settings


router = DefaultRouter()
router.register(r'locations', LocationViewSet)
router.register(r'lost-items', LostItemViewSet)
router.register(r'found-items', FoundItemViewSet)
router.register(r'jobs', JobListingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)