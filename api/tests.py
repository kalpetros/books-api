from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Author
from api.models import Book
from api.models import Publisher


class AuthorTestCase(APITestCase):
    def test_create_author(self):
        """
        Check for author creation
        """
        url = 'http://localhost:8000/api/authors/'
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@doe.com",
            "dob": "1999-10-10"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 1)


class BookTestCase(APITestCase):
    def create_author(self):
        url = 'http://localhost:8000/api/authors/'
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@doe.com",
            "dob": "1999-10-10"
        }
        self.client.post(url, data, format='json')

        author = Author.objects.last()
        return author

    def create_book(self):
        author = self.create_author()

        url = 'http://localhost:8000/api/books/'
        data = {
            "title": "Book",
            "description": "Novel",
            "isbn": "9780544003415",
            "created": "1954-07-29",
            "visibility_status": "AC",
            "author": author.id,
            "publisher": ""
        }
        response = self.client.post(url, data, format='json')

        book = Book.objects.last()
        return response.status_code, book

    def test_create_book(self):
        status_code, book = self.create_book()
        self.assertEqual(status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(book.title, 'Book')

    def test_update_book(self):
        status_code, book = self.create_book()

        self.assertEqual(status_code, status.HTTP_201_CREATED)

        url = f'http://localhost:8000/api/books/{book.id}/'
        data = {
            "title": "Book 2",
            "description": "Novel",
            "isbn": "9780544003415",
            "created": "1954-07-29",
            "visibility_status": "IN",
            "author": '1',
            "publisher": ""
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_book = Book.objects.get(id=book.id)
        self.assertEqual(updated_book.visibility_status, 'IN')
        self.assertEqual(updated_book.title, 'Book 2')

    def test_delete_book(self):
        status_code, book = self.create_book()

        self.assertEqual(status_code, status.HTTP_201_CREATED)

        url = f'http://localhost:8000/api/books/{book.id}/'
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)


class PublisherTestCase(APITestCase):
    def test_create_publisher(self):
        url = 'http://localhost:8000/api/publishers/'
        data = {
            "name": "Publisher",
            "telephone": "555555555",
            "address": "Address"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Publisher.objects.count(), 1)
