from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType

User = get_user_model()


# 1 Category
# 2 Product
# 3 CartProduct
# 4 Cart
# 5 Order

# 6 Customer
# 3 Specification


class Category(models.Model):

    name = models.CharField(max_length=256, verbose_name='Name of categoty')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=256, verbose_name='name')
    category = models.ForeignKey(
        'Category', verbose_name='category', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name='description', null=True)
    image = models.ImageField(verbose_name='image')
    price = models.DecimalField(
        max_digits=9, decimal_places=2, verbose_name='price')

    def __str__(self):
        return self.title


class CartProduct(models.Model):
    product = models.ForeignKey(
        Product, verbose_name='cartproduct', on_delete=models.CASCADE)
    user = models.ForeignKey(
        'Customer', verbose_name='customer', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='cart',
                             on_delete=models.CASCADE, related_name='related_products')
    quantity = models.PositiveIntegerField(default=1, verbose_name="quantity")
    final_price = models.DecimalField(
        max_digits=9, decimal_places=2, verbose_name='total price')

    def __str__(self):
        return f"Product: {self.product.title}(in cart)"


class Cart(models.Model):
    owner = models.ForeignKey(
        'Customer', verbose_name='owner', on_delete=models.CASCADE)
    product = models.ForeignKey(
        CartProduct, blank=True, on_delete=models.CASCADE, related_name='related_cards')
    total_products = models.PositiveIntegerField(default=0)
    total_price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.id


class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name="user",
                             on_delete=models.CASCADE)
    phone = models.CharField(max_length=256, verbose_name='phone number')
    address = models.CharField(max_length=256, verbose_name='address')

    def __str__(self):
        return f'Consumer {self.user.first_name} {self.user.last_name}'


class Specification(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    name = models.CharField(
        max_length=255, verbose_name='name for specefication')

    def __str__(self):
        return f"Specification for {self.name}"
