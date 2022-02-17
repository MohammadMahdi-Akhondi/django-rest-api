from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from . import views

router = routers.DefaultRouter()
router.register('', views.BookView)
router.register('user', views.UserView)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name = 'token_refresh'),
]
