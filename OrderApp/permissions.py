from rest_framework.permissions import BasePermission

class IsAdminOrCustomer(BasePermission):
    def has_permission(self, request, view):
        print('here')
        if request.user.role == 'admin' or request.user.role == 'customer':
            return True
        return False