import os
from django.db import models
from apps.categories.models import Category
from ckeditor.fields import RichTextField
from utils.image_path import upload_products


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Категория',
    )
    title = models.CharField(
        max_length=50,
        verbose_name="Название",
    )
    c = RichTextField(
        verbose_name="Описание",
    )
    image_for_product = models.ImageField(
        upload_to="product_media/",
        blank=True,
        null=True,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создание",
    )

    def __str__(self):
        return self.title


