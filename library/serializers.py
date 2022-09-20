from dataclasses import field
from unittest import mock
from rest_framework import serializers

from .models import Category

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"
