from django.urls import include, path

app_name = "apis"
urlpatterns = [
    path("auth/", include("helpmehelp.authentication.urls", "authentication")),
    path("users/", include("helpmehelp.users.urls", "users")),
    path("orgs/", include("helpmehelp.orgs.urls", "orgs")),
]
