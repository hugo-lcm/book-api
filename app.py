# 1. objective: create an api that makes available the consultation, creation, editing and deletion of books
# 2. base url - localhost
# 3. endpoints - localhost/books (GET)
#                localhost/books (POST)
#                localhost/books/id (GET)
#                localhost/books/id (PUT)
#                localhost/books (DELETE)

from flask import Flask, jsonify, request

app = Flask(__name__)  # create a flask application with the current filename

books = [
    {
        'id': 1,
        'title': 'Lord of the Rings: The Fellowship of the Ring',
        'author': 'J. R. R. Tolkien'
    },
    {
        'id': 2,
        'title': 'A Song of Ice and Fire',
        'author': 'George R. R. Martin'
    },
    {
        'id': 3,
        'title': 'Norse Mythology',
        'author': 'Neil Gaiman'
    }
]

# consult(all)
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# consult(id)
@app.route('/books/<int:id>', methods=['GET'])
def get_books_by_id(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)

# edit(id)
@app.route('/books/<int:id>', methods=['PUT'])
def edit_book_by_id(id):
    new_book = request.get_json()
    for index, book in enumerate(books):
        if book.get('id') == id:
            books[index].update(new_book)
            return jsonify(books[index])

# add
@app.route('/books', methods=['POST'])
def add_new_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(books)

# delete
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    for index, book in enumerate(books):
        if book.get('id') == id:
            del books[index]
    return jsonify(books)


app.run(port=8000, host='localhost', debug=True)
