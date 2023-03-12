from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.response import Response

from ..models.item import Item
from ..serializers import ItemSerializer, ItemReadSerializer

class ItemsView(generics.ListCreateAPIView):
    """
    A view for seeing all items and creating a single item
    /wastewise/items/
    """
    serializer_class = ItemSerializer

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemReadSerializer(items, many=True)
        return Response({'items': serializer.data})
    
    # create item
    def post(self, request):
        serializer = ItemSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# /items/id
class ItemDetailView(generics.ListCreateAPIView):
    serializer_class = ItemSerializer

    def get(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        serializer = ItemReadSerializer(item)
        return Response(serializer.data)
    
    def patch(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)