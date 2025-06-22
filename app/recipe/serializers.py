"""
Serializers for recipe APIs
"""

from rest_framework import serializers

from core.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """ Serializer for Recipes. """

    class Meta:
        model = Recipe
        fileds = ['id', 'title', 'time_minutes', 'price', 'link']
        readonly_fields = ['id']