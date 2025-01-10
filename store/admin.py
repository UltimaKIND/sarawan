from django.contrib import admin
from slugify import slugify

from store.models import *


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ["id", "category_name", "slug"]
    exclude = ("slug",)

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            parent = form.cleaned_data.get("parent")
            slug = slugify(form.cleaned_data.get("category_name"))
            if parent:
                slug = f"{parent.slug}/{slug}"
            obj.slug = slug
            obj.save()


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ["id", "product_name", "slug"]
    exclude = ("slug",)

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            category = form.cleaned_data.get("category")
            slug = slugify(form.cleaned_data.get("product_name"))
            obj.slug = f"{category.slug}/{slug}"
            obj.save()
