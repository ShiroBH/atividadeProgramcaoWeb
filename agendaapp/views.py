from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'agenda/index.html')
def base(request):
    return render(request, 'agenda/base.html')
