from rest_framework import serializers
from .models import books
 
class booksserializers(serializers.ModelSerializer):
    class Meta:
        model = books
        fields = ['id','Book_Title','Author_Name','Year','Genre']
 