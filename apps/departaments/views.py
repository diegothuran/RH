from django.urls import reverse_lazy

from .models import Departament
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

from apps.employes.models import Employee


class ListDepartaments(ListView):
    model = Departament
    fields = '__all__'

    def get_queryset(self):
        active_company = self.request.user.employee.company
        return Departament.objects.filter(company=active_company)


class CreateDepartament(CreateView):
    model = Departament
    fields = ['name']

    def form_valid(self, form):
        departament = form.save(commit=False)
        departament.company = self.request.user.employee.company
        departament.save()
        return super(CreateDepartament, self).form_valid(form)


class UpdateDepartament(UpdateView):
    model = Departament
    fields = ['name']


class DeleteDepartament(DeleteView):
    model = Departament
    success_url = reverse_lazy('list_departaments')
