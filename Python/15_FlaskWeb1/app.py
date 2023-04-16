from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load the book data from a JSON file
with open('book.json', 'r') as f:
    book_data = json.load(f)

@app.route('/')
def index():
    return "Welcome to the library!"

@app.route('/books')
def show_books():
    # Render a template that displays the list of books
    return render_template('books.html', books=book_data)

# direct call jsonify
@app.route('/books/<int:isbn>', methods=['GET'])
def get_book_by_isbn(isbn):
    for book in book_data['books']:
        if book['isbn'] == str(isbn):
            return jsonify(book)
    return jsonify({'message': 'Book not found.'}), 404

# html template call (using book_details.html )
# @app.route('/books/<int:isbn>')
# def book(isbn):
#     book = None
#     try:
#         for b in book_data['books']:
#             if b['isbn'] == str(isbn):
#                 book = b
#                 break
#         if book:
#             return render_template('book_details.html', book=book)
#         else:
#             return f"Error: No book with ISBN {isbn} found."
#     except Exception as e:
#         return f"Error: {e}"


if __name__ == '__main__':
    app.run(debug=True)
