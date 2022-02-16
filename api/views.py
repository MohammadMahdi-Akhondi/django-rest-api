from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer, UserSerializer

# Create your views here.
class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer