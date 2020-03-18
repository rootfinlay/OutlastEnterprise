from django.shortcuts import render
from .models import *

# Create your views here.
def index(request, *args, **kwargs):
    target_page = './html/index.html'

    return render(request, target_page)

def shoes(request, *args, **kwargs):
    target_page = './html/shoes.html'

    all_shoes = Shoes.objects.all()
    all_accessories = Accessories.objects.all()
    all_clothes = Clothing.objects.all()

    context = {
    "all_shoes" : all_shoes,
    "all_accessories" : all_accessories,
    "all_clothing" : all_clothes,
    }

    return render(request, target_page, context)

def error_404(request, exception):
    return render(request,'./html/404.html')


def error_500(request):
    return render(request,'./html/500.html')
