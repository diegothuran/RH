from django.urls import path
from .views import CreateDocument

urlpatterns = [
    path('new/<int:employee_id>/', CreateDocument.as_view(), name='create_document'),
    # path('delete/<int:pk>', DeleteDocument.as_view(), name='delete_document'),
]
