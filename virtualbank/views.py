from django.shortcuts import render

# Create your views here.
def welcome(request):
    context = {"name": "Rajesh"}
    return render(request, 'virtualbank/welcome.html', context)


def greeting(request):
    return render(request, 'virtualbank/greeting.html')


