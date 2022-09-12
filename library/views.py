from functools import partial
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .models import Category
from . import serializers
from rest_framework import viewsets, status
from rest_framework.response import Response

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.
class CategoryViewSet(viewsets.ViewSet):
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the `format=None` keyword argument for each action.
    """
    serializer_class = serializers.CategorySerializer

    def list(self, request):
        queryset = Category.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Category.objects.all()
        obj = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(obj)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Category.objects.all()
        obj = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(instance=obj, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        queryset = Category.objects.all()
        obj = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(instance=obj, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Category.objects.all()
        instance = get_object_or_404(queryset, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
