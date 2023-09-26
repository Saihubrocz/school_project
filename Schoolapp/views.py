from django.shortcuts import render

# All business logic will be written here
def home(request):
    return render(request, 'home.html')