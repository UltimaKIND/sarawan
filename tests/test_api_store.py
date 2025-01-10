import pytest
from rest_framework import status
from rest_framework.test import force_authenticate
from rest_framework.test import APIRequestFactory
from store.models import *
from users.models import *
from store.views import *



class TestCategory():
    '''
    тесты эндпоинтов CRUD API Node
    '''
    @pytest.mark.django_db
    def test_create(self):
        factory = APIRequestFactory()
        view = CategoryViewSet.as_view({'post': 'create'})
        test_user = User.objects.create(email='test_1@sky.pro', password=123456)
        request = factory.post('/category/', {'category_name': 'test_1'}, format='json')
        force_authenticate(request, user=test_user)
        response = view(request)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    @pytest.mark.django_db
    def test_admin_create(self):
        factory = APIRequestFactory()
        view = CategoryViewSet.as_view({'post': 'create'})
        test_user = User.objects.create(email='admin@sarawan.ru', password=123456, is_superuser=True)
        request = factory.post('/category/', {'category_name': 'test_1'}, format='json')
        force_authenticate(request, user=test_user)
        response = view(request)
        assert response.status_code == status.HTTP_201_CREATED

    @pytest.mark.django_db
    def test_list(self):
        factory = APIRequestFactory()
        view = CategoryViewSet.as_view({'get': 'list'})
        test_user = User.objects.create(email='test_1@sarawan.ru', password=123456)
        category = Category.objects.create(category_name= 'test_1')
        request = factory.get('/category/')
        force_authenticate(request, user=test_user)
        response = view(request)
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_retrieve(self):
        factory = APIRequestFactory()
        view = CategoryViewSet.as_view({'get': 'retrieve'})
        test_user = User.objects.create(email='test_1@sarawan.ru', password=123456)
        category = Category.objects.create(category_name= 'test_1')
        request = factory.get('/category/')
        force_authenticate(request, user=test_user)
        response = view(request, pk=category.pk)
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_update(self):
        factory = APIRequestFactory()
        view = CategoryViewSet.as_view({'put': 'update'})
        test_user = User.objects.create(email='test_1@sarawan.ru', password=123456)
        category = Category.objects.create(category_name= 'test_1')
        request = factory.put('/category/', {'category_name': 'test_2'})
        force_authenticate(request, user=test_user)
        response = view(request, pk=category.pk)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    @pytest.mark.django_db
    def test_admin_update(self):
        factory = APIRequestFactory()
        view = CategoryViewSet.as_view({'put': 'update'})
        test_user = User.objects.create(email='admin@sarawan.ru', password=123456, is_superuser=True)
        category = Category.objects.create(category_name= 'test_1')
        request = factory.put('/category/', {'category_name': 'test_2'})
        force_authenticate(request, user=test_user)
        response = view(request, pk=category.pk)
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_delete(self):
        factory = APIRequestFactory()
        view = CategoryViewSet.as_view({'delete': 'destroy'})
        test_user = User.objects.create(email='test_1@sarawan.ru', password=123456)
        category = Category.objects.create(category_name= 'test_1')
        request = factory.delete('/category/')
        force_authenticate(request, user=test_user)
        response = view(request, pk=category.pk)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    @pytest.mark.django_db
    def test_admin_delete(self):
        factory = APIRequestFactory()
        view = CategoryViewSet.as_view({'delete': 'destroy'})
        test_user = User.objects.create(email='admin@sarawan.ru', password=123456, is_superuser=True)
        category = Category.objects.create(category_name= 'test_1')
        request = factory.delete('/category/')
        force_authenticate(request, user=test_user)
        response = view(request, pk=category.pk)
        assert response.status_code == status.HTTP_204_NO_CONTENT

class TestProduct():
    '''
    тесты эндпоинтов CRUD Product
    '''

    @pytest.mark.django_db
    def test_create(self):
        factory = APIRequestFactory()
        view = ProductViewSet.as_view({'post': 'create'})
        test_user = User.objects.create(email='test_1@sarawan.ru', password=123456)
        category = Category.objects.create(category_name= 'test_1')
        request = factory.post('/product/', {'product_name':'test', 'category':category.pk}, format='json')
        force_authenticate(request, user=test_user)
        response = view(request)
        assert response.status_code == status.HTTP_403_FORBIDDEN


    @pytest.mark.django_db
    def test_admin_create(self):
        factory = APIRequestFactory()
        view = ProductViewSet.as_view({'post': 'create'})
        test_user = User.objects.create(email='admin@sarawan.ru', password=123456, is_superuser=True)
        category = Category.objects.create(category_name= 'test_1')
        request = factory.post('/product/', {'product_name':'test', 'category':category.pk}, format='json')
        force_authenticate(request, user=test_user)
        response = view(request)
        assert response.status_code == status.HTTP_201_CREATED

    @pytest.mark.django_db
    def test_list(self):
        factory = APIRequestFactory()
        view = ProductViewSet.as_view({'get': 'list'})
        test_user = User.objects.create(email='test_1@sarawan.ru', password=123456)
        category = Category.objects.create(category_name= 'test_1')
        product = Product.objects.create(product_name= 'test_1', category=category)
        request = factory.get('/product/')
        force_authenticate(request, user=test_user)
        response = view(request)
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_retrieve(self):
        factory = APIRequestFactory()
        view = ProductViewSet.as_view({'get': 'retrieve'})
        test_user = User.objects.create(email='test_1@sarawan.ru', password=123456)
        category = Category.objects.create(category_name= 'test_1')
        product = Product.objects.create(product_name= 'test_1', category=category)
        request = factory.get('/product/')
        force_authenticate(request, user=test_user)
        response = view(request, pk=product.pk)
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_update(self):
        factory = APIRequestFactory()
        view = ProductViewSet.as_view({'put': 'update'})
        test_user = User.objects.create(email='test_1@sarawan.ru', password=123456)
        category = Category.objects.create(category_name= 'test_1')
        product = Product.objects.create(product_name= 'test_1', category=category)
        request_update = factory.put('/product/', {'product_name': 'test_2', 'category': category})
        force_authenticate(request_update, user=test_user)
        response = view(request_update, pk=product.pk)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    @pytest.mark.django_db
    def test_admin_update(self):
        factory = APIRequestFactory()
        view = ProductViewSet.as_view({'put': 'update'})
        test_user = User.objects.create(email='admin@sarawan.ru', password=123456, is_superuser=True)
        category = Category.objects.create(category_name= 'test_1')
        product = Product.objects.create(product_name= 'test_1', category=category)
        request_update = factory.put('/product/', {'product_name': 'test_2', 'category': category})
        force_authenticate(request_update, user=test_user)
        response = view(request_update, pk=product.pk)
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_delete(self):
        factory = APIRequestFactory()
        view = ProductViewSet.as_view({'delete': 'destroy'})
        test_user = User.objects.create(email='test_1@sarawan.ru', password=123456)
        category = Category.objects.create(category_name= 'test_1')
        product = Product.objects.create(product_name= 'test_1', category=category)
        request = factory.delete('/product/')
        force_authenticate(request, user=test_user)
        response = view(request, pk=product.pk)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    @pytest.mark.django_db
    def test_admin_delete(self):
        factory = APIRequestFactory()
        view = ProductViewSet.as_view({'delete': 'destroy'})
        test_user = User.objects.create(email='admin@sarawan.ru', password=123456, is_superuser=True)
        category = Category.objects.create(category_name= 'test_1')
        product = Product.objects.create(product_name= 'test_1', category=category)
        request = factory.delete('/product/')
        force_authenticate(request, user=test_user)
        response = view(request, pk=product.pk)
        assert response.status_code == status.HTTP_204_NO_CONTENT

