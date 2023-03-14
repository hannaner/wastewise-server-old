from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.response import Response

from ..models.spot import Spot
from ..serializers import SpotSerializer, SpotReadSerializer, SpotWriteSerializer

class SpotsView(generics.ListCreateAPIView):
    """
    Display all spots and create a spot
    /spots/
    """
    serializer_class = SpotSerializer

    def get(self, request):
        """View all spots"""
        spots = Spot.objects.filter(owner=request.user.id)
        # spots = spots.items_set
        serializer = SpotSerializer(spots, many=True)
        return Response({ 'spots': serializer.data })
    
    def post(self, request):
        """Create Spot"""
        print('getting into post method')
        serializer = SpotWriteSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'spot': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SpotDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SpotSerializer

    def get(self, request, pk):
        """View single spot with all items associated"""
        spot = get_object_or_404(Spot, pk=pk)
        serializer = SpotSerializer(spot)
        return Response({'spot': serializer.data})
    
    def patch(self, request, pk):
        """Update single spot"""
        spot = get_object_or_404(Spot, pk=pk)
        serializer = SpotSerializer(spot, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        """Delete single spot"""
        spot = get_object_or_404(Spot, pk=pk)
        
        spot.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)