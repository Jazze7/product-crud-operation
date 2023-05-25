from django.contrib.auth.models import User

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

@api_view(["POST"])
@permission_classes([AllowAny])
def create(request):
    email = request.data["email"]
    name = request.data["name"]
    password = request.data["password"]

    print(email)
    print(name)
    print(password)

    if not User.objects.filter(username=email).exists():
        User.objects.create_user(
            username=email, first_name=name, password=password)
        response_data = {
            "status_code": "6000",
            "message": "account created successfully"
        }
        return (response_data)
    else:
        response_data = {
            "status_code": "6001",
            "message": "account already exists"
        }
        return Response(response_data)
