from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


schema_view = get_schema_view(
   openapi.Info(
      title="JerseyWorld API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [

   # ------------------------------------------------------
   # ------------------ Main App---------------------------
   # ------------------------------------------------------
   path('', include('core.urls')),



   # ------------------------------------------------------
   # ------------------ Custom ----------------------------
   # ------------------------------------------------------
    path('admin/', admin.site.urls),
    path('api/',  include('api.urls')),

   # ------------------------------------------------------
   # ------------------ Custom ----------------------------
   # ------------------------------------------------------
    path('api/auth/', include('dj_rest_auth.urls')),

   # ------------------------------------------------------
   # ------------------ JWT ------------------------------
   # ------------------------------------------------------
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


   # ------------------------------------------------------
   # ------------------ SWAGGER ---------------------------
   # ------------------------------------------------------

    # SWAGGER UI
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
