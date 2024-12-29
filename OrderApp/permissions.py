from rest_framework.permissions import BasePermission

class IsAdminOrCustomer(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'admin':
            return True
        if request.user.role == 'customer' and request.user.id == view.kwargs['customer_id']:
            return True
        return False