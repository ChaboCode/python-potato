from django.shortcuts import render


def hello_nerv(request):
    return render(request, 'Serv/hello_nerv.html', {})
