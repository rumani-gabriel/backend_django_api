from django.urls import path, include
from .views import ServiceViewSet, UserViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('services', ServiceViewSet, basename = 'services' )
router.register('users', UserViewSet)

urlpatterns =[
    path('api/', include(router.urls)), 
    
]