from django.core.management import BaseCommand
from users.models import User
from store.serializers import ProductSerializer, CategorySerializer
from store.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        root_node = CategorySerializer(data={'category_name': 'root_category'})
        root_node.is_valid()
        root_node.save()

        root_category = Category.objects.get(category_name='root_category')
        sub_node = CategorySerializer(data={'category_name': 'sub_category', 'parent': root_category.id})
        sub_node.is_valid()
        sub_node.save()

        sub_category = Category.objects.get(category_name='sub_category')
        last_node = CategorySerializer(data={'category_name': 'last_category', 'parent': sub_category.id})
        last_node.is_valid()
        last_node.save()

        last_category = Category.objects.get(category_name='last_category')

        products_list = [
            {'product_name': 'product_1', 'category': root_category.id, 'price': 50.12},
            {'product_name': 'product_2', 'category': root_category.id, 'price': 60.23},
            {'product_name': 'product_3', 'category': sub_category.id, 'price': 70.34},
            {'product_name': 'product_4', 'category': sub_category.id, 'price': 80.45},
            {'product_name': 'product_5', 'category': last_category.id, 'price': 90.56},
            {'product_name': 'product_6', 'category': last_category.id, 'price': 100.67},
        ]
        for product in products_list:
            product_for_create = ProductSerializer(data=product)
            product_for_create.is_valid()
            product_for_create.save()

