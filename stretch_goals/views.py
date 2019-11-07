from django.shortcuts import render

# Create your views here.

def home(request):
    greeting = "Hello, there."
    return render(request, "stretch_goals/home.html", {'greeting': greeting})
    
