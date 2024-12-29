from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from ..models import Order
from rest_framework.authtoken.models import Token

CustomUser = get_user_model()

# API Test Class
class OrderListViewTest(APITestCase):
    def setUp(self):
        self.admin_user = CustomUser.objects.create_user(username='adminuser', password='adminpass123', role='admin')
        self.customer_user = CustomUser.objects.create_user(username='customeruser', password='custpass123', role='customer')

        # Create orders for the customer
        self.order1 = Order.objects.create(
            product_name='Product A',
            quantity=2,
            total_price=500.00,
            customer=self.customer_user
        )

        self.order2 = Order.objects.create(
            product_name='Product B',
            quantity=1,
            total_price=300.00,
            customer=self.customer_user
        )

        self.admin_token = Token.objects.create(user=self.admin_user)
        self.customer_token = Token.objects.create(user=self.customer_user)

    def test_admin_can_view_all_orders(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.admin_token.key)
        response = self.client.get('/orders/')  # Adjust endpoint as necessary

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verify total count in the paginated response
        self.assertEqual(response.data['count'], 2)  # Total number of orders in the database
        
        # Verify the number of results on the first page
        self.assertEqual(len(response.data['results']), 2)

    def test_customer_can_view_own_orders(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.customer_token.key)
        response = self.client.get('/orders/')  # Adjust endpoint as necessary

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verify total count in the paginated response
        self.assertEqual(response.data['count'], 2)  # Total number of orders for this customer
        
        # Verify the number of results on the first page
        self.assertEqual(len(response.data['results']), 2)
        
        # Verify all orders belong to the authenticated customer
        self.assertTrue(
            all(order['customer'] == self.customer_user.username for order in response.data['results'])
        )

    def test_unauthenticated_user_cannot_access_orders(self):
        response = self.client.get('/orders/')  # Adjust endpoint as necessary

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
