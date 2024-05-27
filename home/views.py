from django.shortcuts import render

# Create your views here.
def indexpage(request):
    return render(request, 'index.html')

def contactpage(request):
    return render(request, 'contact.html')

def teampage(request):
    return render(request, 'team.html')

def productpage(request):
    return render(request, 'productsDetails.html')

