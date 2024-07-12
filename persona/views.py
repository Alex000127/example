from django.shortcuts import render
from persona.models import persona

# Create your views here.
def index(request):
    return render(request,"persona/index.html", {
        "personas": persona.objects.all()
    })