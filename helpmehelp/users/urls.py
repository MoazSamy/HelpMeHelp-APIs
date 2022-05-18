from django.urls import path

from helpmehelp.users.apis import CreateUserAPI, UpdateUserAPI, UserDetailsAPI

app_name = "users"
urlpatterns = [
    path("create/", CreateUserAPI.as_view(), name="create_user"),
    path("<int:user_id>/", UserDetailsAPI.as_view(), name="get_user"),
    path("<int:user_id>/update/", UpdateUserAPI.as_view(), name="update_user"),
]
