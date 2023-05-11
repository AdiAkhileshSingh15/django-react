from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"blogs", views.blogView)
urlpatterns = router.urls
