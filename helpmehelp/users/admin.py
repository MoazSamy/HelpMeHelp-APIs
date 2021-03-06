from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from helpmehelp.users.forms import UserAdminChangeForm, UserAdminCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Personal info"),
            {"fields": ("name", "age", "phone", "blood", "address", "nat_ID")},
        ),
        (
            _("Permissions"),
            {
                "fields": ("is_verified",),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["email", "name", "is_verified"]
    search_fields = ["name"]
    ordering = ("email",)
