import mysql.connector
from db_config import DB_CONFIG

def books_grouped_by_genre():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("SELECT genre, COUNT(*) FROM books GROUP BY genre")
    results = cursor.fetchall()
    conn.close()

    print("\nBooks grouped by genre:")
    for genre, count in results:
        print(f"{genre}:{count} books")


def search_books_by_keyword():
    keyword = input("\nEnter a keyword to search: ").strip()
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    query = """
    SELECT title, author, genre
    FROM books
    WHERE title LIKE %s OR author LIKE %s
    """

    like_pattern = f"%{keyword}"
    cursor.execute(query, (like_pattern, like_pattern))
    results = cursor.fetchall()
    conn.close()

    print(f"\nSearch results for'{keyword}':")
    if results:
        for title, author, genre in results:
            print(f" - {title} by {author} ({genre})")
        else:
            print("No matches found.")

if __name__ == "__main__":
    while True:
        print("\n=== Library Menu ===")
        print("1. Show books grouped by genre")
        print("2. Search books by keyword")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            books_grouped_by_genre()
        elif choice == "2":
            search_books_by_keyword()
        elif choice == "3":
            print("Goodybe!")
            break
        else:
            print("Invalid choice. Please try again.")