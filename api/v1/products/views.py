from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from products.models import Product
from api.v1.products.serializers import ProductSerializer


@api_view(["GET"])
@permission_classes([AllowAny])
def ProductView(request):
    instance = Product.objects.all()
    context = {
        "request": request
    }
    serializer = ProductSerializer(instance, many=True, context=context)
    response_data = {
        "status_code": 6000,
        "data": serializer.data
    }
    return Response(response_data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_product(request):
    print(request.user)
    request.data["user"] = request.user
    serializer = ProductSerializer(
        data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save(user=request.user)

        response_data = {
            "status_code": 6000,
            "message": "successfully added product"

        }
        return Response(response_data)
    else:
        response_data = {
            "status_code": 6001,
            "message": "validation error",
            "error": serializer.errors

        }
        return Response(response_data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def edit_product(request, pk):
    if Product.objects.filter(pk=pk).exists():
        instance = Product.objects.get(pk=pk)
        request.data["user"] = request.user
        serializer = ProductSerializer(
            instance=instance, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)

            response_data = {
                "status_code": 6000,
                "message": "successfully edited product"

            }
            return Response(response_data)
    else:
        response_data = {
            "status_code": 6001,
            "message": "validation error",
            "error": serializer.errors

        }
        return Response(response_data)
