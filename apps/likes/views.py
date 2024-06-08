from django.shortcuts import render, redirect

from apps.likes.models import Like

from django.views.generic import (
    CreateView,
    DeleteView,
)


class LikeCreateView(CreateView):
    model = Like
    form_class = Like
    template_name = 'likes_create.html'
    success_url = '/'


class LikeDeleteView(DeleteView):
    model = Like
    template_name = 'likes_delete.html'
    success_url = '/'
