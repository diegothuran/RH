from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('employee/', include('apps.employes.urls')),
    path('departament/', include('apps.departaments.urls')),
    path('account/', include('django.contrib.auth.urls')),
    path('company/', include('apps.companies.urls')),
    path('document/', include('apps.documents.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
