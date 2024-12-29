from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from django.shortcuts import get_object_or_404

from .models import Order
from .serializers import *
from .permissions import * 

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

class OrderDetailByProductNameView(generics.RetrieveAPIView):
    serializer_class = ReadOrderSerializer
    permission_classes = [IsAuthenticated,IsOwner]
    authentication_classes = [TokenAuthentication]  

    def get_object(self):
        product_name = self.kwargs['product_name']
        order = get_object_or_404(Order, product_name=product_name, customer=self.request.user)
        return order
    
class OrderUpdateByProductNameView(generics.UpdateAPIView):
    serializer_class = UpdateOrderSerializer
    permission_classes = [IsAuthenticated,IsOwner]
    authentication_classes = [TokenAuthentication]  

    def get_object(self):
        product_name = self.kwargs['product_name']
        order = get_object_or_404(Order, product_name=product_name, customer=self.request.user)
        return order

class OrderDeleteByProductNameView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated,IsOwner]
    authentication_classes = [TokenAuthentication]  

    def get_object(self):
        product_name = self.kwargs['product_name']
        order = get_object_or_404(Order, product_name=product_name, customer=self.request.user)
        return order