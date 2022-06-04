from django.shortcuts import get_object_or_404

from helpmehelp.orgs.models import Organisation


def get_org(org_id: int) -> Organisation:
    return get_object_or_404(Organisation, pk=org_id)
