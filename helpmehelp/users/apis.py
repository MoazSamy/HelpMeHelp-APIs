from rest_framework import permissions, serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from helpmehelp.users.selectors import get_user
from helpmehelp.users.services import create_user, update_user


class CreateUserAPI(APIView):
    permission_classes = [permissions.AllowAny]

    class InputSerializer(serializers.Serializer):
        username = serializers.CharField()
        name = serializers.CharField()
        password = serializers.CharField()
        email = serializers.CharField()
        age = serializers.CharField()
        phone = serializers.CharField()
        blood = serializers.CharField()
        address = serializers.CharField()
        nat_ID = serializers.CharField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        create_user(**serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)


class UserDetailsAPI(APIView):
    class OutputSerializer(serializers.Serializer):
        username = serializers.CharField()
        name = serializers.CharField()
        email = serializers.EmailField()
        age = serializers.CharField()
        phone = serializers.CharField()
        blood = serializers.CharField()
        address = serializers.CharField()
        nat_ID = serializers.CharField()
        is_verified = serializers.BooleanField()

    def get(self, request, user_id):
        user = get_user(user_id)
        serializer = self.OutputSerializer(user)
        return Response(serializer.data)


class UpdateUserAPI(APIView):
    class InputSerializer(serializers.Serializer):
        name = serializers.CharField(required=False)
        email = serializers.EmailField(required=False)
        phone = serializers.CharField(required=False)

    def post(self, request, user_id):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = get_user(user_id)

        update_user(
            user=user,
            performed_by=request.user,
            data=serializer.validated_data,
        )
        return Response(status=status.HTTP_200_OK)
