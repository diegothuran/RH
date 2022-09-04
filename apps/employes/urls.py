from django.urls import path
from .views import ListEmployees, EditEmployees, DeleteEmployees, NewEmployee

urlpatterns = [
    path('', ListEmployees.as_view(), name='list_employees'),
    path('new', NewEmployee.as_view(), name='create_employee'),
    path('edit/<int:pk>/', EditEmployees.as_view(), name='update_employee'),
    path('delete/<int:pk>/', DeleteEmployees.as_view(), name='delete_employee'),
]
