from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .models import Order
from .serializers import OrderSerializer,ReadOrderSerializer
from .permissions import IsAdminOrCustomer 

class OrderListView(generics.ListAPIView):
    serializer_class = ReadOrderSerializer
    permission_classes = [IsAuthenticated, IsAdminOrCustomer]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        if self.request.user.role == 'admin':
            print('admin')
            return Order.objects.all()
        print('customer')
        return Order.objects.filter(customer=self.request.user)

class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated,IsAdminOrCustomer]
    authentication_classes = [TokenAuthentication]  
    
    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)