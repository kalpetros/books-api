from rest_framework import viewsets

from api.models import Book, Author, Publisher

from api.serializers import AuthorSerializer
from api.serializers import BookDetailSerializer
from api.serializers import BookListSerializer
from api.serializers import BookSerializer
from api.serializers import PublisherSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """
    create:
    Create a new author instance.
    """
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    http_method_names = ['post']


class BookViewSet(viewsets.ModelViewSet):
    """
    create:
    Create a new book instance.

    list:
    Return a list of all books having a publishing company.

    retrieve:
    Return a book.

    update:
    Update a book.

    destroy:
    Delete a book.
    """
    serializer_class = BookSerializer
    list_serializer_class = BookListSerializer
    detail_serializer_class = BookDetailSerializer
    queryset = Book.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            if hasattr(self, 'detail_serializer_class'):
                return self.detail_serializer_class
        elif self.action == 'list':
            if hasattr(self, 'list_serializer_class'):
                return self.list_serializer_class
        else:
            return super().get_serializer_class()

    def get_queryset(self):
        if self.action == 'list':
            queryset = self.queryset.filter(
                visibility_status='AC',
                publisher__isnull=False,
            ).order_by('author__last_name', '-isbn')

            return queryset
        return self.queryset


class PublisherViewSet(viewsets.ModelViewSet):
    """
    create:
    Create a new publisher instance.
    """
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()
    http_method_names = ['post']
