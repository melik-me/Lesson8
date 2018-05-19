import pytest
import requests

@pytest.fixture
def fixt1():
    print("\nInitialization of fixture")
    fixture = "I am a fixture"
    yield fixture
    print("\nDestroying of fixture")

@pytest.fixture(scope="session")
def base_url():
    return "http://pulse-rest-testing.herokuapp.com/"

books = [
            {"title": "blabla", "author": "sdfds"},
            {"title": "$%^&%&", "author": "blabla"},
            {"title": "blabla", "author": "243324"}
        ]


@pytest.fixture(params=books, ids=[str(b) for b in books])
def book(base_url, request):
    book = request.param
    yield book
    if "id" in book:
        requests.delete(base_url + "books/" + str(book["id"]))

@pytest.fixture()
def book_init():
   book_data = {"title": "$%^&%&", "author": "sdfds"}
   r = requests.post(base_url + 'books/', data=book_data)
   book_data = r.json()
   yield book_data
   if "id" in book_data.keys():
       requests.delete(base_url + 'books/' + str(book_data["id"]))