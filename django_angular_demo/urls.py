from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers

from .api import views


router = routers.DefaultRouter()
router.register(r'annotations', views.AnnotationViewSet)


urlpatterns = [
    url(r'^$', views.index),
    url(r'^api/auth/', include('rest_auth.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
