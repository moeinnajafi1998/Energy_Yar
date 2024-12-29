from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .models import Order
from .serializers import OrderSerializer
from .permissions import IsAdminOrCustomer 

class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated,IsAdminOrCustomer]
    authentication_classes = [TokenAuthentication]  
    
    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)