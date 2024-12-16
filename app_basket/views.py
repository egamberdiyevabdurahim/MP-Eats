from django.views import View
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from app_common.premissions import IsOwnerOrReadOnly
from .serializers import BasketSerializer
from .models import BasketModel
from app_common.pagination import CustomPagination


class BasketView(APIView):
    serializer_class = BasketSerializer
    queryset = BasketModel.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        basket = self.queryset.filter(user=request.user)
        serializer = self.serializer_class(basket, many=True)
        response = {
            'success': True,
            'data': serializer.data,
        }
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        baskets = BasketModel.objects.get(user=request.user)
        print(baskets)
        serializer = self.serializer_class(data=request.data, user=request.user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success': True,
            'data': serializer.data,
        }
        return Response(response, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        basket = self.queryset.get(id=kwargs['pk'], user=request.user)
        serializer = self.serializer_class(basket, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success': True,
            'data': serializer.data,
        }
        return Response(response, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        basket = self.queryset.get(id=kwargs['pk'], user=request.user)
        basket.delete()
        response = {
            'success': True,
            'message': 'Basket deleted successfully',
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)


class ChangeBasketStatusView(View):
    queryset = BasketModel.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

