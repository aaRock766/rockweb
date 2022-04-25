from django.shortcuts import render

# Create your views here.
def f_index(request):
    render(request,'f-index.html')