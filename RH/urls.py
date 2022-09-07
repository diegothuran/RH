from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('employee/', include('apps.employes.urls')),
    path('departaments/', include('apps.departaments.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('companies/', include('apps.companies.urls')),
]
