from django.shortcuts import render


def about(request):
    return render(request, 'help/about.html', {})


def privacy(request):
    return render(request, 'help/privacy.html', {})


def faq(request):
    return render(request, 'help/faq.html', {})
