import pytest
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate

from store.models import *
from store.views import *
from users.models import *


class TestCategory:
    """
    тесты эндпоинтов CRUD API Node
    """

    @pytest.mark.django_db
    def test_create(self):
        factory = APIRequestFactory()
        view = NodeViewSet.as_view({"post": "create"})
        test_user = User.objects.create(email="test_1@sky.pro", password=123456)
        request = factory.post(
            "/retail_pad",
            {
                "name": "test_1",
                "email": "test_1email@sky.pro",
                "country": "test_1",
                "city": "test_1",
                "street": "test_1",
                "house": "1",
            },
            format="json",
        )
        force_authenticate(request, user=test_user)
        response = view(request)
        assert response.status_code == status.HTTP_201_CREATED

    @pytest.mark.django_db
    def test_list(self):
        factory = APIRequestFactory()
        view = NodeViewSet.as_view({"get": "list"})
        test_user = User.objects.create(email="test_1@sky.pro", password=123456)
        node = Node.objects.create(
            name="test_1",
            email="test_1email@sky.pro",
            country="test_1",
            city="test_1",
            street="test_1",
            house="1",
        )
        request = factory.get("/retail_pad")
        force_authenticate(request, user=test_user)
        response = view(request)
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_retrieve(self):
        factory = APIRequestFactory()
        view = NodeViewSet.as_view({"get": "retrieve"})
        test_user = User.objects.create(email="test_1@sky.pro", password=123456)
        node = Node.objects.create(
            name="test_1",
            email="test_1email@sky.pro",
            country="test_1",
            city="test_1",
            street="test_1",
            house="1",
        )
        request = factory.get("/retail_pad")
        force_authenticate(request, user=test_user)
        response = view(request, pk=node.pk)
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_update(self):
        factory = APIRequestFactory()
        view = NodeViewSet.as_view({"put": "update"})
        test_user = User.objects.create(email="test_1@sky.pro", password=123456)
        node = Node.objects.create(
            name="test_1",
            email="test_1email@sky.pro",
            country="test_1",
            city="test_1",
            street="test_1",
            house="1",
        )
        request = factory.put(
            "/retail_pad/",
            {
                "name": "test_2",
                "email": "test_2email@sky.pro",
                "country": "test_2",
                "city": "test_2",
                "street": "test_2",
                "house": "2",
            },
        )
        force_authenticate(request, user=test_user)
        response = view(request, pk=node.pk)
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_delete(self):
        factory = APIRequestFactory()
        view = NodeViewSet.as_view({"delete": "destroy"})
        test_user = User.objects.create(email="test_1@sky.pro", password=123456)
        node = Node.objects.create(
            name="test_1",
            email="test_1email@sky.pro",
            country="test_1",
            city="test_1",
            street="test_1",
            house="1",
        )
        request = factory.delete("/retail_pad/")
        force_authenticate(request, user=test_user)
        response = view(request, pk=node.pk)
        assert response.status_code == status.HTTP_204_NO_CONTENT


class TestProduct:
    """
    тесты эндпоинтов CRUD Product
    """

    @pytest.mark.django_db
    def test_create(self):
        factory = APIRequestFactory()
        view = ProductViewSet.as_view({"post": "create"})
        test_user = User.objects.create(email="test_1@sky.pro", password=123456)
        request = factory.post(
            "/product", {"name": "test", "model": "test"}, format="json"
        )
        force_authenticate(request, user=test_user)
        response = view(request)
        assert response.status_code == status.HTTP_201_CREATED

    @pytest.mark.django_db
    def test_list(self):
        factory = APIRequestFactory()
        view = ProductViewSet.as_view({"get": "list"})
        test_user = User.objects.create(email="test_1@sky.pro", password=123456)
        product = Product.objects.create(name="test_1", model="test_1")
        request = factory.get("/product")
        force_authenticate(request, user=test_user)
        response = view(request)
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_retrieve(self):
        factory = APIRequestFactory()
        view = ProductViewSet.as_view({"get": "retrieve"})
        test_user = User.objects.create(email="test_1@sky.pro", password=123456)
        product = Product.objects.create(name="test_1", model="test_1")
        request = factory.get("/product")
        force_authenticate(request, user=test_user)
        response = view(request, pk=product.pk)
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_update(self):
        factory = APIRequestFactory()
        view = ProductViewSet.as_view({"put": "update"})
        test_user = User.objects.create(email="test_1@sky.pro", password=123456)
        product = Product.objects.create(name="test_1", model="test_1")
        request_update = factory.put("/product/", {"name": "test_2", "model": "test_2"})
        force_authenticate(request_update, user=test_user)
        response = view(request_update, pk=product.pk)
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_delete(self):
        factory = APIRequestFactory()
        view = ProductViewSet.as_view({"delete": "destroy"})
        test_user = User.objects.create(email="test_1@sky.pro", password=123456)
        product = Product.objects.create(name="test_1", model="test_1")
        request = factory.delete("/retail_pad/")
        force_authenticate(request, user=test_user)
        response = view(request, pk=product.pk)
        assert response.status_code == status.HTTP_204_NO_CONTENT
