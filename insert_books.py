import mysql.connector
import requests
from db_config import DB_CONFIG

GENRES = [
    "python programming",
    "fantasy",
    "science",
    "history",
    "self-help",
    "romance"
]

def fetch_books_from_openlibrary(query, limit=40):
    url = f"https://openlibrary.org/search.json?q={query}&limit={limit}"
    response = requests.get(url)
    data = response.json()
    books = []
    for doc in data.get("docs", []):
        title = doc.get("title")
        author = ", ".join(doc.get("author_name", [])) if doc.get("author_name") else "Unknown Author"
        genre = query.title()
        if title:
            books.append((title, author, genre, 5))
    return books  # <-- moved outside the loop

def insert_books_into_db(books):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.executemany(
        "INSERT INTO books (title, author, genre, total_copies) VALUES (%s, %s, %s, %s)",
        books
    )
    conn.commit()
    conn.close()

if __name__ == "__main__":
    all_books = []
    for genre in GENRES:
        print(f"Fetching books for: {genre}")
        books = fetch_books_from_openlibrary(genre, limit=40)
        all_books.extend(books)

    print(f"Inserting {len(all_books)} books into database...")
    insert_books_into_db(all_books)
    print("Done!")
