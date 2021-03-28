# Books API

## Getting started

To run the books API application open a terminal and type:

```
$ docker-compose up
```

## Documentation

Visit http://localhost:8000 to see details about the available endpoints.

## Schema

Visit http://localhost:8000/schema/ to display the OpenAPI schema.

## Tests

To run tests type:

```
$ docker-compose run --rm --no-deps api python manage.py test
```

## Endpoints

### authors/

#### POST

Create a new author:

```
$ curl -H 'Content-Type: application/json;' --request POST --data '{"first_name": "John", "last_name": "Doe", "email": "john@doe.com", "dob": "1999-10-10"}' http://localhost:8000/api/authors/
```

### books/

#### POST

Create a new book:

```
$ curl -H 'Content-Type: application/json;' --request POST --data '{"title": "Book", "description": "Novel", "isbn": "9780544003415", "created": "1954-07-29", "visibility_status": "AC", "author": "int:author_id", "publisher": "int:publisher_id"}' http://localhost:8000/api/books/
```

#### GET

Get a list of all books:

```
$ curl -H 'Accept: application/json;' http://localhost:8000/api/books/
```

### books/{id}/

#### GET

Get book details:

```
$ curl -H 'Accept: application/json;' http://localhost:8000/api/books/{id}/
```

#### PUT

Update a book:

```
$ curl -H "Content-Type: application/json" -X PUT --data '{"title":"LOTR2", "isbn":"9782436541425", "created": "1954-12-12", "author": "int:author_id", "publisher": "int:publisher_id"}' http://localhost:8000/api/books/{id}/
```

#### DELETE

```
$ curl -H "Content-Type: application/json" -X DELETE http://localhost:8000/api/books/{id}/
```

### publishers/

#### POST

Create a new publisher:

```
$ curl -H 'Content-Type: application/json;'--request POST --data '{"name": "Publisher", "telephone": "555555555", "address": "Address"}' http://localhost:8000/api/publishers/
```
