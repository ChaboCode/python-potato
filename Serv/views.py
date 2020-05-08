from django.shortcuts import render


def hello_nerv(req):
    return render(req, 'Serv/hello_nerv.html', {})
