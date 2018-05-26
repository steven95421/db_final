from django.shortcuts import render

# Create your views here.


def anncs(request):
    return render(request, 'anncs.html')
