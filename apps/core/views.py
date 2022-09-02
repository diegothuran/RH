from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.employes.models import Employee


@login_required
def home(request):
    data = dict()
    data['user'] = request.user
    return render(request, 'core/templates/index.html', data)
