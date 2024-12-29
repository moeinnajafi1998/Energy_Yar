from .views import *
from django.urls import path

urlpatterns = [
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/create/', OrderCreateView.as_view(), name='order-create'),
    path('orders/<str:product_name>/', OrderDetailByProductNameView.as_view(), name='order-detail-by-product-name'),
    # path('orders/<int:pk>/update/', views.OrderUpdateView.as_view(), name='order-update'),
    # path('orders/<int:pk>/delete/', views.OrderDeleteView.as_view(), name='order-delete'),

]
