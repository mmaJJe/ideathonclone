from django.shortcuts import render

# Create your views here.
def managehome(request):
    return render(request, "managehome.html")