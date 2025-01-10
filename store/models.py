from django.db import models

from users.models import User

# константа для полей с возможными нулевыми значениями
NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    """
    модель категории
    """

    category_name = models.CharField(max_length=100, verbose_name="название категории")
    description = models.TextField(verbose_name="описание категории", **NULLABLE)
    parent = models.ForeignKey(
        "self",
        verbose_name="родительская категория",
        related_name="childs",
        on_delete=models.CASCADE,
        **NULLABLE,
    )
    slug = models.SlugField(max_length=500, unique=True, **NULLABLE)
    image = models.ImageField(verbose_name="изображение категории", **NULLABLE)

    def __str__(self):
        return f"{self.pk}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ("category_name",)


class Product(models.Model):
    """
    модель продукта
    """

    product_name = models.CharField(max_length=100, verbose_name="название продукта")
    description = models.TextField(verbose_name="описание продукта", **NULLABLE)
    category = models.ForeignKey(
        Category, verbose_name="категория продукта", on_delete=models.CASCADE
    )
    slug = models.SlugField(max_length=500, unique=True, **NULLABLE)
    price = models.DecimalField(max_digits=10, decimal_places=2, **NULLABLE)
    first_image = models.ImageField(
        verbose_name="1-ое изображение продукта", **NULLABLE
    )
    second_image = models.ImageField(
        verbose_name="2-ое изображение продукта", **NULLABLE
    )
    third_image = models.ImageField(
        verbose_name="3-ое изображение продукта", **NULLABLE
    )

    def __str__(self):
        return f"{self.pk} - {self.product_name}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ("product_name",)


class Cart(models.Model):
    """
    Модель корзины
    """

    user = models.ForeignKey(
        User, verbose_name="пользователь", on_delete=models.CASCADE
    )
    cart_data = models.JSONField(**NULLABLE)
