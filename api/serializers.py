from rest_framework import serializers

from api.models import Author
from api.models import Book
from api.models import Publisher


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        exclude = ('id', )


class AuthorCustomSerializer(serializers.ModelSerializer):
    dob = serializers.DateField('%d/%m/%Y')

    class Meta:
        model = Author
        fields = ['name', 'email', 'dob']


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        exclude = ('id', )


class PublisherCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name', 'address']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    def get_author(self, obj):
        return f'{obj.author.first_name} {obj.author.last_name}'

    class Meta:
        model = Book
        fields = ['title', 'description', 'isbn', 'author']


class BookDetailSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    publisher = serializers.SerializerMethodField()
    created = serializers.DateField(format='%d/%m/%Y')
    author = AuthorCustomSerializer()
    publisher = PublisherCustomSerializer()

    class Meta:
        model = Book
        fields = [
            'title', 'description', 'isbn', 'created', 'author', 'publisher'
        ]
