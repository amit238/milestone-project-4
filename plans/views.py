from django.shortcuts import render
from .models import Plans
# Create your views here.


def plans(request):

    ''' View that renders plans page '''

    plans = Plans.objects.all()
    return render(request, 'plans/plans.html', {'plans': plans})
