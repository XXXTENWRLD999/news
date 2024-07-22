from django.shortcuts import render
from .models import News,Category

# Create your views here.
def index(request):
    news = News.objects.all()
    category = Category.objects.all()
    return render(request,'index.html',{'new':news,'cat':category})



def single(request,id):
    news = News.objects.get(id=id)
    return render(request,'single.html',{'new':news})





def category(request):
    return render(request,'category.html')

def contact(request):
    return render(request,'contact.html')


