from django.shortcuts import render, redirect
from django.contrib import messages
from apps.buy.models import UserProfile
from apps.buy.forms import CardForm


def update_card(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = CardForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Информация о карте успешно обновлена.')
            return redirect('profile')
    else:
        form = CardForm(instance=user_profile)
    return render(request, 'salud/checkout.html', {'form': form})


def successful_payment(request):
    return render(request, 'salud/payment-successful.html')
