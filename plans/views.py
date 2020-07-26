from django.shortcuts import render
from .models import Plans
# Create your views here.

def plans(request):
    

    plans = Plans.objects.all()
    return render(request, 'plans/plans.html', { 'plans' : plans })