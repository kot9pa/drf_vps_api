from rest_framework import routers, permissions
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import VPSViewSet


router = routers.SimpleRouter()
router.register(r'vps', VPSViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="VPS API",
        default_version='v1',
        description="VPS API documentation",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0),
         name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    path('v1/', include(router.urls)),
]
