from rest_framework import permissions

from .permissions import StaffEditorPermission


class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser, StaffEditorPermission]