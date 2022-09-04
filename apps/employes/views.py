from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
)
from .models import Employee


class ListEmployees(ListView):
    model = Employee

    def get_queryset(self):
        active_company = self.request.user.employee.company
        return Employee.objects.filter(company=active_company)


class EditEmployees(UpdateView):
    model = Employee
    fields = '__all__'


class DeleteEmployees(DeleteView):
    model = Employee
    success_url = reverse_lazy('list_employees')


class NewEmployee(CreateView):
    model = Employee
    fields = ['name', 'departament']

    def form_valid(self, form):
        employee = form.save(commit=False)
        username = employee.name.split(' ')[0] + employee.name.split(' ')[0]
        employee.company = self.request.user.employee.company
        employee.user = User.objects.create(username=username)
        employee.save()
        return super(NewEmployee, self).form_valid(form)