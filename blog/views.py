from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.shortcuts import HttpResponse, get_object_or_404
from rest_framework.response import Response
from .serializers import *
from .models import *

# Create your views here.


def home(request):
    return HttpResponse("Django Blog App")


class PostListCreate(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRUD(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
