# from django.shortcuts import render, redirect
# from django.views.generic import ListView, CreateView, DetailView
# from apps.trainer.models import Trainer, AboutUs
# from apps.trainer.forms import TrainerForm, AboutUsForm
# from django.urls import reverse_lazy

# from django.views import generic


# # class TrainerListView(ListView):
# #     model = Trainer
# #     template_name = 'salud/trainner.html'
# #     context_object_name = 'trainer'


# class TrainerListView(ListView):
#     model = Trainer
#     template_name = 'salud/trainner.html'
#     context_object_name = 'trainer'


# # class TrainerAddView(DetailView):
# #     model = Trainer
# #     template_name = 'salud/trainner.html'
# #     context_object_name = 'trainer'


# class TrainerAddView(CreateView):
#     model = Trainer
#     form_class = TrainerForm
#     template_name = 'salud/trainner.html'
#     success_url = reverse_lazy('trainer_list')

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


# class AboutUsView(ListView):
#     model = AboutUs
#     template_name = 'salud/about.html'
#     context_object_name = 'about'


# def trainner_details(request):
#     return render(request, 'salud/trainner-details.html')





# class TrainerCreateView(generic.CreateView):
#     model = Trainer
#     form_class = TrainerForm
#     template_name = 'trainer/trainer_create.html'
#     success_url = '/shop/'


# class TrainerUpdateView(generic.UpdateView):
#     model = Trainer
#     form_class = TrainerForm
#     template_name = 'trainer/trainer_update.html'
#     success_url = '/shop/'


# class TrainerDeleteView(generic.DeleteView):
#     model = Trainer
#     template_name = 'trainer/trainer_delete.html'
#     success_url = '/shop/'


# def shop(request):
#     return render(request, 'salud/shop.html')



from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.trainer.models import Trainer, AboutUs
from apps.trainer.forms import TrainerForm, AboutUsForm

class TrainerListView(ListView):
    model = Trainer
    template_name = 'salud/trainner.html'
    context_object_name = 'trainers'

class TrainerCreateView(CreateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainer/trainer_create.html'
    success_url = reverse_lazy('trainer')

class TrainerUpdateView(UpdateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainer/trainer_update.html'
    success_url = reverse_lazy('trainer')

class TrainerDeleteView(DeleteView):
    model = Trainer
    template_name = 'trainer/trainer_delete.html'
    success_url = reverse_lazy('trainer')

class AboutUsView(ListView):
    model = AboutUs
    template_name = 'salud/about.html'
    context_object_name = 'about'

def trainner_details(request):
    return render(request, 'salud/trainner-details.html')

def shop(request):
    return render(request, 'salud/shop.html')
