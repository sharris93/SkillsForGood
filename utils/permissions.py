from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    
    # This method is executed whenever we run `self.check_object_permissions()` from our views
    # If you use Generics views then this will be called automatically
    def has_object_permission(self, request, view, obj):
        # Allow GET requests (as well as OPTIONS and HEAD) full access to routes using this permissions class
        if request.method in SAFE_METHODS:
            return True
        
        # If NOT a GET request, then check the user is the owner of the object
        return request.user == obj.owner