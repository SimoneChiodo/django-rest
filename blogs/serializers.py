from rest_framework import serializers
from .models import Blog, Comment

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = "__all__" # Seleziono tutti i campi

class BlogSerializer(serializers.ModelSerializer):
  comments = CommentSerializer(many=True, read_only=True) # Prendo anche i commenti del blog
  class Meta:
    model = Blog
    fields = "__all__"
