from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView

from apps.categories.models import Category
from apps.products.forms import ProductForm
from apps.products.models import Product
from apps.trainer.models import Trainer


class indexView(TemplateView):
    template_name = 'salud/index.html'


class ProductListView(generic.ListView):
    model = Product
    template_name = 'salud/shop.html'
    context_object_name = 'products'


def shop_single(request):
    return render(request, 'salud/shop-single.html')


def shop(request):
    return render(request, 'salud/shop.html')


# class ProductDetailView(generic.DetailView):
#     model = Product
#     template_name = 'salud/shop-single.html'
#     context_object_name = 'product'


class ProductCreateView(generic.CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_create.html'
    success_url = '/shop/'


class ProductUpdateView(generic.UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_update.html'
    success_url = '/shop/'


class ProductDeleteView(generic.DeleteView):
    model = Product
    template_name = 'product/product_delete.html'
    success_url = '/shop/'


def shop(request):
    return render(request, 'salud/shop.html')
