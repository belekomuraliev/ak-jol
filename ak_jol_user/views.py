
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Author, User
from .serializers import AuthorSerializer


class AuthorRegisterAPIView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

