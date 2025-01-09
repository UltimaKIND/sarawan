import json
from decimal import Decimal
from store.models import Product, Cart

class CartService(object):

    def __init__(self, request):
        '''
        Иницилизицаия корзины
        '''
        self.user = request.user
        self.cart = Cart.objects.filter(user=self.user).first()
        self.data = json.loads(self.cart.cart_data) if self.cart.cart_data else {}

    def __len__(self):
        '''
        возвращает количество товаров в корзине
        '''
        return sum(int(item['quantity']) for item in self.data.values()) if self.data else 0

    def add(self, product, quantity=1, update_quantity=False):
        '''
        добавляет выбранный товар в корзину
        '''
        product = Product.objects.get(id=product)
        product_id = product.id
        if self.data:
            if product_id not in self.data.keys():
                self.data[product_id] = {'quantity': 0, 'price': str(product.price)}
        else:
            self.data = {}
            self.data[product_id] = {'quantity': 0, 'price': str(product.price)}
        if update_quantity:
            self.data[product_id]['quantity'] = quantity
        else:
            self.data[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        '''
        сохраняет данные корзины в модели
        '''
        self.cart.cart_data = json.dumps(self.data)
        self.cart.save()


    def remove(self, product):
        '''
        удаляет выбраный товар из корзины
        '''
        if str(product) in self.data.keys():
            del self.data[str(product)]
            self.save()

    def get_total_price(self):
        '''
        возвращает сумму всех товаров в корзине
        '''
        return str(sum(Decimal(item['price']) * int(item['quantity']) for item in self.data.values())) if self.data else 'cart is empty'

    def clear(self):
        '''
        очищает корзину
        '''
        self.data = None
        self.save()

    def get_data(self):
        '''
        возвращает список всех товаров в корзине, их цену на момент добавления в корзину и количество
        '''
        return ({product.id: {"price": self.data[str(product.id)]['price'], "quantity": self.data[str(product.id)]['quantity']}} for product in Product.objects.filter(id__in=self.data.keys())) if self.data else 'cart is empty'
