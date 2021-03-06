from django.urls import path

from helpmehelp.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
)

app_name = "app_users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:name>/", view=user_detail_view, name="detail"),
]
