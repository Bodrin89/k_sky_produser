from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.check.urls')),
    path('docs/swagger', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path('docs/schema', SpectacularAPIView.as_view(), name='schema'),
]

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]
