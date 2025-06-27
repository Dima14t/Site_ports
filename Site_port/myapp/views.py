from django.shortcuts import render

# Create your views here.
from .models import Myapp_Model


def index(request):
    works = Myapp_Model.objects.all()
    return render(request, 'myapp/index.html', {'works': works})


