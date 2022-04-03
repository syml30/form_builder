from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

from django.urls import path, include, re_path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Form Builder Service API",
        default_version='v0.01',
        description="This service is used to Form Builder",
        contact=openapi.Contact(email=""),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/form_buiders/', include('form_builders.urls')),
                  re_path(r'^api/doc(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
                          name='documentation_json'),
                  re_path(r'^api/doc/$', schema_view.with_ui('swagger', cache_timeout=0), name='documentation'),
                  re_path(r'^api/redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema_redoc'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
