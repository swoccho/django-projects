from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='authentication:login page')
def homepage(request):

    return render(request, 'homepage/homepage.html')



@login_required(login_url='authentication:login page')
def show_all_products(request):
    return render(request,'products/all_products.html')

@login_required(login_url='authentication:login page')
def sell_history(request):
    return render(request,'history/sell_history.html')


@login_required(login_url='authentication:login page')
def purchase_history(request):
    return render(request,'history/purchase_history.html')








