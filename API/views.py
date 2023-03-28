from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from API.models import Author, Book
from API.serializers import AuthorSerializer, BookSerializer

# Create your views here.
@api_view(['GET'])
def getData(request):
    author = Author.objects.all()
    serializer = AuthorSerializer(author, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


class GetBook(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, author_id):
        book = Book.objects.filter(author_id=author_id)
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def add_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def update_book(request, book_id):

    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = BookSerializer(book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    book.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)