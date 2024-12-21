from django.shortcuts import render
from .models import books
from .serializers import booksserializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
 
# Create your views here.
@api_view(['POST'])
def book_list(request):
    if request.method == 'POST':
        serializer = booksserializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors)
 
@api_view(['GET','PUT','DELETE'])
def book_id(request,id):
    book_list = books.objects.get(pk=id)
 
    if request.method == 'GET':
        serializer = booksserializers(book_list)
        print(serializer.data)
    elif request.method == 'PUT':
        serializer = booksserializers(book_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        book_list.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    return Response(serializer.data)
