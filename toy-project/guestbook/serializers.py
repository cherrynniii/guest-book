###Model Serializer case
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):

  class Meta:
    model = Post
    fields = "__all__"

class PostDelSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Post
    fields = ['password']