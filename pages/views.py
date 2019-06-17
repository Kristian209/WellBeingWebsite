from django.shortcuts import render

# Create your views here.
def home(request):
    title = 'Home'
    context = {
    'title': title
    }
    return render(request, "home.html", context)

def about(request):
    title = 'About'
    context = {
    'title': title
    }
    return render(request, "about.html", context)

def contact(request):
    title = 'Contact'
    context = {
    'title': title
    }
    return render(request, "contact.html", context)
