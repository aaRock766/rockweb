from django.shortcuts import render

# Create your views here.
def f(request):
    return render(request,'f-index.html')


def reg(request):
    return render(request, 'f-register.html')
