from django.urls import path
from rest_framework.routers import DefaultRouter
from django.conf.urls import include
from .views import MealViewSet, RatingViewSet , UserViewset

router = DefaultRouter()
router.register('meals', MealViewSet)
router.register('ratings', RatingViewSet)
router.register('users', UserViewset)

urlpatterns = [
    path('' , include(router.urls)),
]