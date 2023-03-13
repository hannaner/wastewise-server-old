from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from ..models.spot import Spot
from ..serializers import SpotSerializer, SpotReadSerializer, SpotWriteSerializer

class SpotsView(generics.ListCreateAPIView):
    """
    Display all spots and create a spot
    /spots/
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = SpotSerializer

    def get(self, request):
        """View all spots"""
        spots = Spot.objects.filter(owner=request.user.id)
        serializer = SpotReadSerializer(spots, many=True)
        return Response({ 'spots': serializer.data })
    
    def post(self, request):
        """Create Spot"""
        request.data['spot']['owner'] = request.user.id
        serializer = SpotWriteSerializer(data=request.data['spot'])
        print(serializer)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'spot': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SpotDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = SpotSerializer

    def get(self, request, pk):
        """View single spot"""
        spot = get_object_or_404(Spot, pk=pk)
        
        if request.user != spot.owner:
            raise PermissionDenied('Unauthorized access')
        
        serializer = SpotReadSerializer(spot)
        return Response({'spot': serializer.data})
    
    def patch(self, request, pk):
        """Update single spot"""
        spot = get_object_or_404(Spot, pk=pk)
        serializer = SpotSerializer(spot, data=request.data)

        if request.user != spot.owner:
            raise PermissionDenied('Unauthorized access')

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        """Delete single spot"""
        spot = get_object_or_404(Spot, pk=pk)
        
        if request.user != spot.owner:
            raise PermissionDenied('Unauthorized access')
        
        spot.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)