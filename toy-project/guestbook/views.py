from django.shortcuts import render
from django.http import JsonResponse # 추가 
from django.shortcuts import get_object_or_404 # 추가
from django.views.decorators.http import require_http_methods
from guestbook.models import *
import json
from datetime import datetime, timedelta, date # 날짜
from .serializers import * # type: ignore
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.core.exceptions import ValidationError

class PostList(APIView):
    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        posts = Post.objects.all().order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
class PostDetail(APIView):
    def get(self, request, id):
        post = get_object_or_404(Post, id=id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def put(self, request, id):
        post = get_object_or_404(Post, id=id)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid(): 
            if post.password == request.data.get('password'):
                serializer.save()
                return Response(serializer.data)
            else:
                return JsonResponse({'message':'비밀번호가 올바르지 않습니다.'}, status=400)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self,request,id):
        post = get_object_or_404(Post, id=id)
        serializer = PostDelSerializer(post, data=request.data)
        if serializer.is_valid():
            if post.password == request.data.get('password'):
                post.delete()
                return JsonResponse({'message':'success'}, status=204)
            else:
                return JsonResponse({'message':'비밀번호가 올바르지 않습니다.'}, status=400)
        return Response(status=status.HTTP_204_NO_CONTENT)