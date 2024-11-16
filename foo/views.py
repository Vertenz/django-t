from django.http import HttpResponse

def index(request):
    return HttpResponse('foo home')

def second(request):
    return HttpResponse('second foo home')