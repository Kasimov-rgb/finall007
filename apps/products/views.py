from django.shortcuts import render
from django.views import generic

from apps.categories.models import Category
from apps.products.models import Product
from apps.trainer.models import Trainer


class ProductListView(generic.ListView):
    model = Product
    template_name = 'salud/index.html'
    context_object_name = 'products'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['left_categories'] = Category.objects.filter(parent=None)
        context['dumbbells_product'] = Product.objects.filter(category__title='Гантели')[:5]
        context['protein_product'] = Product.objects.filter(category__title='Протойн')[:5]
        context['sportswear_product'] = Product.objects.filter(category__title='Спортивная одежда')[:5]
        context['traners'] = Trainer.objects.all()[:3]

        return context

def shop_single(request):
    return render(request, 'salud/shop-single.html')


def shop(request):
    return render(request, 'salud/shop.html')
