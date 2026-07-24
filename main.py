import os
from flask import Flask, render_template, request

app= Flask(__name__)

books={
  001:{"name" : "Harry Porter", "status": "Available"}
}

def check_book(book_id):
  try:
    book_id= int(book_id)
    if book_id on books:
      book=books[book_id]
      return f"Book: {book['name']}, Status: {book['status']"}
    return "Invalid"

  except ValueError:
    return "Invalid"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    book_id = request.form.get('book', '')
    result = check_book(book_id)
    return render_template('index.html', result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
