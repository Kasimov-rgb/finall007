from django.views import generic
from django.shortcuts import render, redirect

from apps.basket.models import Basket, Item

from apps.basket.models import Favorite
from apps.basket.forms import AddToFavoriteForm


class BasketDetailView(generic.ListView):
    template_name = 'salud/shop-cart.html'
    context_object_name = 'basket'

    def get_queryset(self):
        return Basket.objects.get(user=self.request.user)


class QuantityChangeLogics:

    @staticmethod
    def minus_quantity(request, pk):
        item = Item.objects.get(id=pk)
        if item.quantity - 1 == 0:
            item.delete()
            return redirect('basket')
        item.quantity -= 1
        item.save()
        return redirect('basket')

    def plus_quantity(request, pk):
        item = Item.objects.get(id=pk)
        item.quantity += 1
        item.save()
        return redirect('basket')


def add_to_favorite(request, product_id):
    if request.method == 'POST':
        form = AddToFavoriteForm(request.POST)
        if form.is_valid():
            favorite = form.save(commit=False)
            favorite.user = request.user
            favorite.product_id = product_id
            favorite.save()
            return redirect('product_detail', product_id=product_id)
    else:
        form = AddToFavoriteForm()
    return render(request, 'salud/shop-cart.html', {'form': form})


def remove_from_favorite(request, favorite_id):
    favorite = Favorite.objects.get(id=favorite_id)
    favorite.delete()
    return redirect('favorites_list')


class BasketListView(generic.ListView):
    model = Basket
    template_name = 'salud/shop-cart.html'
