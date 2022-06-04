from django.db import models
from django.utils.translation import gettext_lazy as _

from helpmehelp.users.models import User


class Organisation(models.Model):
    class Meta:
        db_table = "organisations"
        verbose_name = "org"
        verbose_name_plural = "orgs"

    name = models.CharField(_("Organisation Name"), max_length=155)
    logo = models.URLField(_("Oragnisation Logo URL"), max_length=200)
    email = models.EmailField(
        _("Organisation Email"), max_length=155, unique=True, blank=True
    )
    phone = models.CharField(
        _("Organisation Phone Number"), max_length=12, null=True, blank=True
    )
    address = models.CharField(
        _("Organisation Address"), max_length=200, null=True, blank=True
    )
    description = models.CharField(_("Organisation Description"), max_length=500)
    user = models.ForeignKey(User, verbose_name="Admin", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
