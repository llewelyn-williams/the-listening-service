from django.shortcuts import render


def index(request):
    """ The view for the index page. """
    return render(request, "home/index.html")


def about(request):
    """ The view for the about page. """
    return render(request, "home/about.html")
