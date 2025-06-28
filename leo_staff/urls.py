from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_api import StaffViewSet, ManagerViewSet, InternViewSet

router = DefaultRouter()
router.register(r'staff', StaffViewSet)
router.register(r'managers', ManagerViewSet)
router.register(r'interns', InternViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

