from django.shortcuts import render

# Create your views here.
# All business logic will be written here
def home(request):
    return render(request, 'home.html')