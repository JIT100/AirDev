from django.contrib import admin
from django.urls import path,include
from account.api import index
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="AirDev Todo API Endpoint",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
allurls = [
    path('admin/', admin.site.urls),
    path("api-auth/", include("rest_framework.urls")), 
    path('auth/',include('account.urls')),
    path('todo/',include('todo.urls'))
]
urlpatterns = allurls + [
    path('', index),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]