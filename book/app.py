from flask import Flask, jsonify, request
from models import load_books, save_books

app = Flask(__name__)

@app.get("/api/books")
def list_books():
    return jsonify(load_books())

@app.post("/api/books")
def add_book():
    data = request.get_json(silent=True) or {}
    title = data.get("title")
    author = data.get("author")
    if not title or not author:
        return jsonify({"error": "title and author are required"}), 400

    books = load_books()
    new_id = (max([b["id"] for b in books]) + 1) if books else 1
    book = {"id": new_id, "title": title, "author": author}
    books.append(book)
    save_books(books)
    return jsonify(book), 201

@app.put("/api/books/<int:book_id>")
def update_book(book_id):
    data = request.get_json(silent=True) or {}
    books = load_books()
    for b in books:
        if b["id"] == book_id:
            b["title"] = data.get("title", b["title"])
            b["author"] = data.get("author", b["author"])
            save_books(books)
            return jsonify(b)
    return jsonify({"error": "not found"}), 404

@app.delete("/api/books/<int:book_id>")
def delete_book(book_id):
    books = load_books()
    new_books = [b for b in books if b["id"] != book_id]
    if len(new_books) == len(books):
        return jsonify({"error": "not found"}), 404
    save_books(new_books)
    return jsonify({"status": "deleted"})

if __name__ == "__main__":
    app.run(debug=True)
