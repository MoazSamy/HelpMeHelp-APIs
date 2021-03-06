from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from helpmehelp.users.usermanager import CustomUserManager


class User(AbstractUser):
    blood_types = [
        ("O+", "O Positive"),
        ("O-", "O Negative"),
        ("A+", "A Positive"),
        ("A-", "A Negative"),
        ("B+", "B Positive"),
        ("B-", "B Negative"),
        ("AB+", "AB Positive"),
        ("AB-", "AB Negative"),
    ]
    name = models.CharField(_("User Full Name"), max_length=155)
    email = models.EmailField(_("Email"), max_length=155, unique=True, blank=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    phone = models.CharField(_("Phone Number"), max_length=12, null=True, blank=True)
    blood = models.CharField(
        _("Blood Type"), max_length=3, choices=blood_types, null=True, blank=True
    )
    address = models.CharField(_("User Address"), max_length=200, null=True, blank=True)
    nat_ID = models.CharField(
        _("National ID"), max_length=14, unique=True, null=True, blank=True
    )
    is_verified = models.BooleanField(_("Is user verified by email"), default=False)
    date_joined = models.DateTimeField(default=now)
    USERNAME_FIELD = "email"
    username = None
    first_name = None
    last_name = None
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def get_absolute_url(self) -> str:

        return reverse("users:get_user", args={str(self.id)})
