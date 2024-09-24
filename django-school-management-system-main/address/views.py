from django.shortcuts import render, redirect
from .models import District
from .forms import DistrictForm


def add_district(request):
    forms = DistrictForm()
    if request.method == 'POST':
        forms = DistrictForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('district')
    district = District.objects.all()
    context = {'forms': forms, 'district': district}
    return render(request, 'address/district.html', context)
