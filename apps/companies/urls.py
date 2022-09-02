from django.urls import path
from .views import CreateCompanyView, EditCompanyView


urlpatterns = [
    path('new', CreateCompanyView.as_view(), name='create_company'),
    path('edit/<int:pk>',
         EditCompanyView.as_view(), name='edit_company'),
]
