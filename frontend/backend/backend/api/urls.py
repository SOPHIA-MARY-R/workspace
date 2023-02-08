from images.api.views import ImageViewSets
from rest_framework import routers
from django.urls import path, include

router=routers.DefaultRouter()
router.register('images', ImageViewSets)

urlpatterns=[
    path('', include(router.urls))
]