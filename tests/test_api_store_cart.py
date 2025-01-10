import pytest
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate

from store.models import *
from store.views import *
from users.models import *


class TestCart:
    """
    тесты Cart
    """

    @pytest.mark.django_db
    def test_post_add_product_to_cart(self):
        factory = APIRequestFactory()
        view = CartAPI.as_view()
        test_user = User.objects.create(email="test_1@sky.pro", password=123456)
        cart = Cart.objects.create(user=test_user)
        category = Category.objects.create(category_name="test_1")
        product = Product.objects.create(product_name="test_1", category=category)
        request = factory.post("/cart/", {"product": product.pk}, format="json")
        force_authenticate(request, user=test_user)
        response = view(request)
        assert response.status_code == status.HTTP_202_ACCEPTED

    @pytest.mark.django_db
    def test_post_update_product_in_cart(self):
        factory = APIRequestFactory()
        view = CartAPI.as_view()
        test_user = User.objects.create(email="test_1@sky.pro", password=123456)
        cart = Cart.objects.create(user=test_user)
        category = Category.objects.create(category_name="test_1")
        product = Product.objects.create(product_name="test_1", category=category)
        request_add_product = factory.post(
            "/cart/", {"product": product.pk}, format="json"
        )
        request_update_quantity = factory.post(
            "/cart/",
            {"product": product.pk, "update_quantity": True, "quantity": 5},
            format="json",
        )
        force_authenticate(request_add_product, user=test_user)
        force_authenticate(request_update_quantity, user=test_user)
        response_from_post_add = view(request_add_product)
        response_from_post_update = view(request_update_quantity)
        assert response_from_post_add.status_code == status.HTTP_202_ACCEPTED
        assert response_from_post_update.status_code == status.HTTP_202_ACCEPTED

    @pytest.mark.django_db
    def test_post_remove_product_from_cart(self):
        factory = APIRequestFactory()
        view = CartAPI.as_view()
        test_user = User.objects.create(email="test_1@sky.pro", password=123456)
        cart = Cart.objects.create(user=test_user)
        category = Category.objects.create(category_name="test_1")
        product_1 = Product.objects.create(
            product_name="test_1", category=category, price=20.1
        )
        product_2 = Product.objects.create(
            product_name="test_2", category=category, price=20.1
        )
        request_add_product_1 = factory.post(
            "/cart/", {"product": product_1.pk}, format="json"
        )
        request_add_product_2 = factory.post(
            "/cart/", {"product": product_2.pk, "quantity": 3}, format="json"
        )
        request_remove_product_2 = factory.post(
            "/cart/", {"product": product_2.pk, "remove": True}, format="json"
        )
        force_authenticate(request_add_product_1, user=test_user)
        force_authenticate(request_add_product_2, user=test_user)
        force_authenticate(request_remove_product_2, user=test_user)
        response_from_post_add_1 = view(request_add_product_1)
        response_from_post_add_2 = view(request_add_product_2)
        response_from_remove = view(request_remove_product_2)
        assert response_from_post_add_1.status_code == status.HTTP_202_ACCEPTED
        assert response_from_post_add_2.status_code == status.HTTP_202_ACCEPTED
        assert response_from_remove.status_code == status.HTTP_202_ACCEPTED

    @pytest.mark.django_db
    def test_post_clear_cart(self):
        factory = APIRequestFactory()
        view = CartAPI.as_view()
        test_user = User.objects.create(email="test_1@sky.pro", password=123456)
        cart = Cart.objects.create(user=test_user)
        category = Category.objects.create(category_name="test_1")
        product_1 = Product.objects.create(
            product_name="test_1", category=category, price=20.1
        )
        product_2 = Product.objects.create(
            product_name="test_2", category=category, price=20.1
        )
        request_add_product_1 = factory.post(
            "/cart/", {"product": product_1.pk}, format="json"
        )
        request_add_product_2 = factory.post(
            "/cart/", {"product": product_2.pk, "quantity": 3}, format="json"
        )
        request_clear_cart = factory.post("/cart/", {"clear": True}, format="json")
        force_authenticate(request_add_product_1, user=test_user)
        force_authenticate(request_add_product_2, user=test_user)
        force_authenticate(request_clear_cart, user=test_user)
        response_from_post_add_1 = view(request_add_product_1)
        response_from_post_add_2 = view(request_add_product_2)
        response_from_post_clear = view(request_clear_cart)
        assert response_from_post_add_1.status_code == status.HTTP_202_ACCEPTED
        assert response_from_post_add_2.status_code == status.HTTP_202_ACCEPTED
        assert response_from_post_clear.status_code == status.HTTP_202_ACCEPTED

    @pytest.mark.django_db
    def test_get_cart(self):
        factory = APIRequestFactory()
        view = CartAPI.as_view()
        test_user = User.objects.create(email="test_1@sky.pro", password=123456)
        cart = Cart.objects.create(user=test_user)
        category = Category.objects.create(category_name="test_1")
        product = Product.objects.create(
            product_name="test_1", category=category, price=20.1
        )
        post_request = factory.post(
            "/cart/",
            {"product": product.pk, "update_quantity": True, "quantity": 5},
            format="json",
        )
        get_request = factory.get("/cart/")
        force_authenticate(post_request, user=test_user)
        force_authenticate(get_request, user=test_user)
        response_from_post = view(post_request)
        response_from_get = view(get_request)
        assert response_from_post.status_code == status.HTTP_202_ACCEPTED
        assert response_from_get.status_code == status.HTTP_200_OK
