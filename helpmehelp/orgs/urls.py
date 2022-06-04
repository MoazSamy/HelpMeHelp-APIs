from django.urls import path

from helpmehelp.orgs.apis import CreateOrgAPI, OrgDetailAPI, UpdateOrgAPI

app_name = "orgs"
urlpatterns = [
    path("create/", CreateOrgAPI.as_view(), name="create_org"),
    path("<int:org_id>/", OrgDetailAPI.as_view(), name="get_org"),
    path("<int:org_id>/update/", UpdateOrgAPI.as_view(), name="update_org"),
]
