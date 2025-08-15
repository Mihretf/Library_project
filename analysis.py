import mysql.connector
from db_config import DB_CONFIG

def fetch_all_books():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor= conn.cursor()

    cursor.execute("SELECT * FROM books")
    books= cursor.fetchall()

    conn.close()
    return books


if __name__ == "__main__":
    books= fetch_all_books()
    for book in books:
        print(book)

def fetch_all_users():
    conn= mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    cursor.execute("SELECT *FROM users")
    users = cursor.fetchall()

    conn.close()
    return users

if __name__ == "__main__":
    users= fetch_all_users()
    for user in users:
        print(user)


def borrowed_books_with_users():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT u.name, b.title, r.borrow_date, r.return_date
        FROM borrow_records r
        JOIN users u ON r.user_id = u.user_id
        JOIN books b ON r.book_id = b.book_id
    """)
    data = cursor.fetchall()
    conn.close()
    return data

if __name__ == "__main__":
    for record in borrowed_books_with_users():
        print(record)
