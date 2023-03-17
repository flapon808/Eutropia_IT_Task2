from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def index(request):
    # return JsonResponse({'foo':'bar'})
    context = {
        "fasion" : [1,2,3]
    }
    return render(request, 'index.html', context=context)