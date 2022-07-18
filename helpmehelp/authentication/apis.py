from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class CustomTokenObtainPairView(TokenObtainPairView):
    class TokenSerializer(TokenObtainPairSerializer):
        @classmethod
        def get_token(cls, user):
            token = super().get_token(user)

            # Users Claims
            token["name"] = user.name
            token["phone"] = user.email
            token["age"] = user.age
            token["phone"] = user.phone
            token["blood"] = user.blood
            token["address"] = user.address
            token["nat_ID"] = user.nat_ID
            return token

    serializer_class = TokenSerializer
