from django.shortcuts import render

# Create your views here.

def home_screate_view(request):
    print(request.headers)
    return render(request, "index.html", {})