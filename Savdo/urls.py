from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path,include
from Asosiy.views import *


router = DefaultRouter()
router.register('suv',SuvViewSet)
router.register('mijoz',MijozViewSet)
router.register('Admin',AdminViewSet)
router.register('haydovchi',HaydovchiViewSet)
router.register('buyurtma',BuyurtmaViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
    path('get_token/', TokenObtainPairView.as_view()),
    path('token_refresh/', TokenRefreshView.as_view())
]
