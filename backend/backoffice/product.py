from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import json
from django.core.paginator import Paginator

from product.models import Product
from .forms import ProductForm


def test(request):
    return render(request, 'product/test_table.html')

def add_product(request):
    current_user = request.user
    url = request.META.get('HTTP_REFERER')  # get last url
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Product added successfully')
            return HttpResponseRedirect(url)
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect(url)
    
    form = ProductForm
    data = Product.objects.all().order_by('-id')[:10]
    context= {
        'form':form,
        'data': data,
    }
    return render(request, 'product/addProduct.html',context)