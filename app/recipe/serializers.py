"""
Serializers for recipe APIs
"""

from rest_framework import serializers

from core.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """ Serializer for Recipes. """

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']  #  Make sure that users can´t change user id from recipe


class RecipeDetailSerializer(RecipeSerializer):
    """ Serializer for recipe detial view."""
    
    class Meta(RecipeSerializer.Meta):
        fields=RecipeSerializer.Meta.fields + ['description']