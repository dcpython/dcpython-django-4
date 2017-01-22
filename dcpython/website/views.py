from django.shortcuts import render

# Create your views here.


def about(request):
    """
    """
    context = {}
    return render(request, 'about.html', context)


def andrew_w_singer(request):
    """
    """
    context = {}
    return render(request, 'andrew-w-singer.html', context)


def coc(request):
    """
    """
    context = {}
    return render(request, 'coc.html', context)


def contact(request):
    """
    """
    context = {}
    return render(request, 'contact.html', context)


def donate(request):
    """
    """
    context = {}
    return render(request, 'donate.html', context)


def home(request):
    """
    """
    context = {}
    return render(request, 'home.html', context)
