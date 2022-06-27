from rest_framework.permissions import SAFE_METHODS, BasePermission


class AuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.user == obj.author
            or request.method in SAFE_METHODS
            or request.user.is_superuser
        )
