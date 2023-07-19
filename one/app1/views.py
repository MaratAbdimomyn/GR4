from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def contacts(request):
    return render(request, "contacts.html")

def about_company(request):
    return render(request, "about_company.html")

