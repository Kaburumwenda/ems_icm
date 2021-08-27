from django.shortcuts import render
from django.utils import timezone
# Create your views here.
def index(request):
    context = {
        
    }
    return render(request, 'base/dashboard.html', context)