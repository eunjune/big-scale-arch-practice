from rest_framework import viewsets,status
from .models import Shop,Order
from .producer import publish
from .serializers import ShopSerializer,OrderSerializer
from rest_framework.response import  Response


class ShopViewSet(viewsets.ViewSet):
    def list(self, request):
        shops = Shop.objects.all()
        serializer = ShopSerializer(shops, many=True)
        publish()
        return Response(serializer.data)

    def create(self, request):
        serializer = ShopSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        shop = Shop.objects.get(id=pk)
        serializer = ShopSerializer(shop)
        return Response(serializer.data)

    def update(self, request, pk=None):
        shop = Shop.objects.get(id=pk)
        serializer = ShopSerializer(instance=shop, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        shop = Shop.objects.get(id=pk)
        shop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderViewSet(viewsets.ViewSet):
    def list(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        pass

    def update(self, request, pk=None):
        order = Order.objects.get(id=pk)
        serializer = OrderSerializer(instance=order, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def retrieve(self, request, pk=None):
        order = Order.objects.get(id=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        order = Order.objects.get(id=pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)