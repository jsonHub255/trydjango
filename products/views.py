from django.core.exceptions import ViewDoesNotExist
from products.models import Product
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm
from django.http import Http404
            
            
# VIEW for update Products
def update_product(request, id):
    obj = Product.objects.get(id=id)
    desi_form = ProductForm(request.POST or None, instance=obj)
    if desi_form.is_valid():
        desi_form.save()
        
    context = {
        "form": desi_form
    }
    return render(request, "products/product_create.html", context)


# VIW TO INSERT FORM DATAS TO THE DB (Method 2)
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


#  View to show product details
def product_dynamic_view(request, id):
    # catch id page IF does not exist(Method 1)
    # objs = get_object_or_404(Product, id=id)
    # catch id page IF does not exist(Method 2)
    try:
        objs = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        "obj": objs
    }
    return render(request, "products/home.html", context)
    
#  VIEW to delete a Single Product
def product_delete_view(request, id):
    # obj = get_object_or_404(Product, id=id)
    try:
        obj = Product.objects.get(id=id)
        if request.method == "POST":
            #  Here we pass a confirming befor the delete action
            obj.delete()
            # redirct after delete
            return redirect('../')
    except Product.DoesNotExist:
        raise Http404
    
    context = {
        "obj": obj
    }
    
    return render(request, "products/product_delete.html", context)
    
#  VIEW to show products list
def procuct_list_view(request):
    querysets = Product.objects.all()
    context = {
        "sets": querysets
    }
    return render(request, "products/product_list.html", context)
    
    
    
    
    
    
    



