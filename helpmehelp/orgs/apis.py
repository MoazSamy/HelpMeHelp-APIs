from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from helpmehelp.orgs.selectors import get_org
from helpmehelp.orgs.services import create_org, update_org


class CreateOrgAPI(APIView):
    class InputSerializer(serializers.Serializer):
        name = serializers.CharField()
        logo = serializers.CharField()
        email = serializers.CharField()
        phone = serializers.CharField()
        address = serializers.CharField()
        description = serializers.CharField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        create_org(user=request.user, **serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)


class OrgDetailAPI(APIView):
    class OutputSerializer(serializers.Serializer):
        name = serializers.CharField()
        email = serializers.EmailField()
        phone = serializers.CharField()
        address = serializers.CharField()
        admin = serializers.CharField(source="user.name")

    def get(self, request, org_id):
        org = get_org(org_id)
        serializer = self.OutputSerializer(org)
        return Response(serializer.data)


class UpdateOrgAPI(APIView):
    class InputSerializer(serializers.Serializer):
        name = serializers.CharField(required=False)
        email = serializers.EmailField(required=False)
        phone = serializers.CharField(required=False)
        address = serializers.CharField(required=False)

    def post(self, request, org_id):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        org = get_org(org_id)

        update_org(
            org=org,
            performed_by=request.user,
            data=serializer.validated_data,
        )
        return Response(status=status.HTTP_200_OK)
