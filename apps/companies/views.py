from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import Company
from django.urls import reverse


class CreateCompanyView(CreateView):
    model = Company
    fields = '__all__'

    def form_valid(self, form):
        obj = form.save()
        employee = self.request.user.employee
        employee.company = obj
        employee.save()
        return reverse('home')


class EditCompanyView(UpdateView):
    model = Company
    fields = '__all__'
