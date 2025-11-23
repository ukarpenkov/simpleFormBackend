from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from workplaces.views import WorkplaceViewSet

router = routers.DefaultRouter()
router.register(r'workplaces', WorkplaceViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
