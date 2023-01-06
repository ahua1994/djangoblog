from django.urls import path
from .views import *

urlpatterns = [
    path("", home),
    path("post/create/", PostListCreate.as_view()),
    path("post/<int:pk>/", PostRUD.as_view())
]
