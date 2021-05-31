from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.http import Http404

# Create your views here.
def index(request):
    today = datetime.today().date()# get today date
    context = {"date":today} #variable funcion
    return render(request, 'foods/index.html', context=context)


def food_detail(request,food):
    context = dict()
    if food == "chicken" :
        context["name"] = "코딩에 빠진 닭"
        context["description"]="주머니가 가벼운 당신에게"
        context["price"]= 25000
        context["img_path"]= "foods/images/chicken.jpg"
    else:
        raise Http404("이런건 없어 이세캬 ")
    return render(request, 'foods/detail.html', context)
