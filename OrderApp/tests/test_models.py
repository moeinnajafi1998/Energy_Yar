from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import Order

CustomUser = get_user_model()

# Model Test Class
class OrderModelTest(TestCase):
    def setUp(self):
        self.customer = CustomUser.objects.create_user(username='testuser', password='password123', role='customer')
        self.order = Order.objects.create(
            product_name='Product A',
            quantity=2,
            total_price=500.00,
            customer=self.customer
        )

    def test_order_creation(self):
        self.assertEqual(self.order.product_name, 'Product A')
        self.assertEqual(self.order.quantity, 2)
        self.assertEqual(self.order.total_price, 500.00)
        self.assertEqual(self.order.customer, self.customer)

    def test_order_string_representation(self):
        self.assertEqual(str(self.order), 'Product A - testuser')
