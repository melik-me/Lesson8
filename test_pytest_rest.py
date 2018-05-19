import requests

def test_create_book_positive(base_url, book):
    response = requests.post(base_url + "books/", data=book)
    assert response.status_code == 201
    body = response.json()
    for key in book:
        assert book[key].strip() == body[key]
    book["id"] = body["id"]

def test_update_book(base_url, init_book):
    pass