from django.urls import path
from .views import (
    Model3dListCreateView,
    Model3dDetailView,
    BadgeListCreateView,
    BadgeDetailView,
    UserProfileListCreateView,
    UserProfileDetailView,
)

urlpatterns = [
    path('models/', Model3dListCreateView.as_view(), name='model3d-list'),
    path('models/<int:pk>/', Model3dDetailView.as_view(), name='model3d-detail'),
    path('badges/', BadgeListCreateView.as_view(), name='badge-list'),
    path('badges/<int:pk>/', BadgeDetailView.as_view(), name='badge-detail'),
    path('profiles/', UserProfileListCreateView.as_view(), name='userprofile-list'),
    path('profiles/<int:pk>/', UserProfileDetailView.as_view(), name='userprofile-detail'),
]
