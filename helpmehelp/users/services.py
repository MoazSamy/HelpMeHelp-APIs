from typing import Dict, Optional

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import PermissionDenied
from django.core.exceptions import ValidationError as DjValidationError
from django.core.validators import validate_email
from django.forms import ValidationError

from helpmehelp.common.services import model_update
from helpmehelp.users.models import User


def create_user(
    *,
    name: str,
    email: str,
    password: str,
    age: Optional[int],
    blood: Optional[str],
    phone: Optional[int],
    address:  Optional[str],
    nat_ID: Optional[int],
) -> User:
    try:
        email = BaseUserManager.normalize_email(email)
        validate_email(email)

        # Readying data for validation
        user: User = User(
            name=name,
            email=email,
            age=age,
            blood=blood,
            phone=phone,
            address=address,
            nat_ID=nat_ID,
        )

        # Validate users password
        validate_password(password, user)
        user.password = make_password(password)

        # Validating user data
        user.full_clean()

        # Passing user data to DB
        user.save()
        return user

    except DjValidationError as e:
        raise ValidationError(e.messages)


def update_user(
    *,
    user: User,
    performed_by: User,
    data: Dict,
) -> User:

    # Making sure the update on user is performed by the requested user
    if user != performed_by:
        raise PermissionDenied()

    # Add more fields here if needed
    non_side_effect_fields = ["name", "phone"]

    # Updating user data in DB
    user, _ = model_update(
        instance=user,
        fields=non_side_effect_fields,
        data=data,
    )

    user.save()

    return user
