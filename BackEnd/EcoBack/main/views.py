from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView, ListAPIView, CreateAPIView
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from .models import *
from .serializers import *
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import time
from PIL import Image
import io
from rest_framework.routers import DefaultRouter, Route, DynamicRoute


used_codes = []

class MyProfileViewSet(viewsets.GenericViewSet, RetrieveAPIView, RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Profile, user=self.request.user)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    @action(methods=['post'], detail=False, permission_classes=[IsAdminUser])
    def register_event(self, request):
        # Implementation for registering an event
        pass


class BarcodeViewSet(viewsets.GenericViewSet, CreateAPIView, ListAPIView):
    queryset = Barcode.objects.all()
    serializer_class = BarcodeSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Existing implementation for creating barcodes
        pass

    @action(methods=['get'], detail=False)
    def count(self, request):
        count = self.get_queryset().count()
        return JsonResponse({'count': count})


class ProductCategoryViewSet(viewsets.GenericViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def brands(self, request, pk=None):
        category = self.get_object()
        brands = Brand.objects.filter(category=category)
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)



class BrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        brand = self.get_object()
        products = Product.objects.filter(brand=brand)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Optionally restricts the returned products to a given brand,
        by filtering against a 'brand' query parameter in the URL.
        """
        queryset = super().get_queryset()
        brand_id = self.request.query_params.get('brand')
        if brand_id is not None:
            queryset = queryset.filter(brand=brand_id)
        return queryset

    @action(detail=True, methods=['get'])
    def detail(self, request, *args, **kwargs):
        product = self.get_object()
        serializer = self.get_serializer(product)
        return Response(serializer.data)

    @action(methods=['post'], detail=False, permission_classes=[IsAdminUser])
    def register_product(self, request):
        # Implementation for registering a product
        pass


class BadgeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = get_object_or_404(Profile, user=self.kwargs['id'])
        return Badge.objects.get(user=user)