from django.shortcuts import render


def rules(request):
    return render(request, 'pages/rules.html')


def about(request):
    return render(request, 'pages/about.html')
