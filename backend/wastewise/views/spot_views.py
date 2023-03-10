from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from ..models.spot import Spot
from ..serializers import SpotSerializer

class Spots(generics.ListCreateAPIView):
    """
    Display all spots and create a spot
    /spots/
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = SpotSerializer

    # View all spots
    def get(self, request):
        spots = Spot.objects.filter(owner=request.user.id)
        data = SpotSerializer(spots, many=True).data
        return Response({ 'spots': data })
    
    def post(self, request):
        request.data['spot']['owner'] = request.user.id
        spot = SpotSerializer(data = request.data['spot'])
        if spot.is_valid():
            spot.save()
            return Response({'spot': spot.data}, status=status.HTTP_201_CREATED)
        return Response(spot.errors, status=status.HTTP_400_BAD_REQUEST)