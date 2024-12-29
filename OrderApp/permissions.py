from rest_framework.permissions import BasePermission

class IsAdminOrCustomer(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'admin' or request.user.role == 'customer':
            return True
        return False
    

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.customer.username == request.user.username