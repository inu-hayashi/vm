from django.shortcuts import render


def index(request):
    return render(request, 'app_vm/index.html')

def kirin(request):
    return render(request, 'app_vm/kirin.html')