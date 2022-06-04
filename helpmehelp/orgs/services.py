from typing import Dict, Optional

from django.core.exceptions import PermissionDenied

from helpmehelp.common.services import model_update
from helpmehelp.orgs.models import Organisation
from helpmehelp.users.models import User


def create_org(
    *,
    name: str,
    logo: str,
    email: Optional[str],
    phone: int,
    address: str,
    user: User,
    description: Optional[str],
) -> Organisation:

    org = Organisation(
        name=name,
        logo=logo,
        email=email,
        phone=phone,
        address=address,
        user=user,
        description=description,
    )
    org.full_clean()
    org.save()
    return org


def update_org(
    *,
    org: Organisation,
    performed_by: User,
    data: Dict,
) -> Organisation:

    # Making sure the update on organisation is performed by admin
    if performed_by != org.user:
        raise PermissionDenied()

    # Add more fields here if needed
    non_side_effect_fields = ["name", "phone", "address"]

    # Updating user data in DB
    org, _ = model_update(
        instance=org,
        fields=non_side_effect_fields,
        data=data,
    )

    org.save()

    return org
