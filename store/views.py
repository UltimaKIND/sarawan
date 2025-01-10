from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsModer
from rest_framework.response import Response
from rest_framework.views import APIView
from store.pagination import Pagination
from store.serializers import *
from store.services import CartService

class CategoryViewSet(viewsets.ModelViewSet):
    """
    контроллер Category
    """
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(parent=None)
    pagination_class = Pagination

    def get(self, request):
            queryset = Category.objects.filter(parent=None)
            paginated_queryset = self.paginate_queryset(queryset)
            serializer = CategorySerializer(paginated_queryset, many=True)
            return self.get_paginated_response(serializer.data)

    def get_permissions(self):
            if self.action in ["create", "update", "destroy"]:
                self.permission_classes = (IsModer, IsAuthenticated)

            return super().get_permissions()

class ProductViewSet(viewsets.ModelViewSet):
    """
    контроллер Product
    """
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    pagination_class = Pagination
    queryset = Product.objects.all()

    def get_permissions(self):
        if self.action in ["create", "update", "destroy"]:
            self.permission_classes = (IsModer, IsAuthenticated)

        return super().get_permissions()

class CartAPI(APIView):
    """
    контроллер для взаимодействия с корзиной
    """
    def get(self, request, format=None):

        cart = CartService(request)

        return Response({'data': cart.get_data(), 'total_products_in_cart': len(cart), 'total_price': cart.get_total_price(), 'user': str(request.user)}, status=status.HTTP_200_OK)

    def post(self, request, **kwargs):

        cart = CartService(request)

        if 'remove' in request.data:
            product = request.data['product']
            cart.remove(product)


        elif 'clear' in request.data:
            cart.clear()

        else:
            product = request.data
            cart.add(product=product['product'], quantity=product['quantity'] if 'quantity' in product else 1, update_quantity=product['update_quantity'] if 'update_quantity' in product else False)

        return Response({'message': 'cart updated'}, status=status.HTTP_202_ACCEPTED)

