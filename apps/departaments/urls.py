from django.contrib import admin
from django.urls import path, include
from .views import (
    ListDepartaments,
    CreateDepartament,
    UpdateDepartament,
    DeleteDepartament
)


urlpatterns = [
    path('list', ListDepartaments.as_view(), name='list_departaments'),
    path('new', CreateDepartament.as_view(), name='create_departaments'),
    path('edit/<int:pk>', UpdateDepartament.as_view(), name='update_departament'),
    path('delete/<int:pk>', DeleteDepartament.as_view(), name='delete_departament'),
]
