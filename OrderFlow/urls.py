from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from OrderApp.permissions import IsAdmin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('OrderApp.urls')),
    
    path('api-token-auth/', views.obtain_auth_token),
]


schema_view = get_schema_view(
   openapi.Info(
      title="ENERGY YAR API",
      default_version='v1',
      description="just smile :)",
      contact=openapi.Contact(email="moeinnajafi1996@gmail.com"),
   ),
   public=True,
   permission_classes=(IsAdmin,),
   
   
)

urlpatterns += [   
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]