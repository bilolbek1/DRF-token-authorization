from django.urls import path
from .views import RegisterAPIView, LoginAPIView, TestAPIView, LogoutAPIView


urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('test/', TestAPIView.as_view(), name='test')
]