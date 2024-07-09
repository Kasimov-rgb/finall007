from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView
from apps.trainer.models import Trainer, AboutUs
from apps.trainer.forms import TrainerForm, AboutUsForm
from django.urls import reverse_lazy


# class TrainerListView(ListView):
#     model = Trainer
#     template_name = 'salud/trainner.html'
#     context_object_name = 'trainer'


class TrainerListView(ListView):
    model = Trainer
    template_name = 'salud/trainner.html'
    context_object_name = 'trainer'


# class TrainerAddView(DetailView):
#     model = Trainer
#     template_name = 'salud/trainner.html'
#     context_object_name = 'trainer'


class TrainerAddView(CreateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'salud/trainner.html'
    success_url = reverse_lazy('trainer_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AboutUsView(ListView):
    model = AboutUs
    template_name = 'salud/about.html'
    context_object_name = 'about'


def trainner_details(request):
    return render(request, 'salud/trainner-details.html')
