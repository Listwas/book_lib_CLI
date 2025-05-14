import json, os

BOOK_STATUSES = {
    'w': 'want to read',
    'r': 'reading',
    'c': 'completed'
}

MENU_OPTIONS = {
    'a': 'add books',
    'l': 'list all books',
    'r': 'remove book',
    'e': 'exit'
}

class Library:
    def __init__(self, file_name):
        self.books = []
        self.args = ['title', 'author', 'pages', 'status']
        self.file_name = file_name
        self.end = ''

        if not os.path.exists(self.file_name):
            with open(self.file_name, 'w') as file:
                json.dump([], file)

        self.load_books_data()

    def load_books_data(self):
        if os.path.getsize(self.file_name) > 0:
            with open(self.file_name, 'r') as file:
                self.books = json.load(file)

    def save_books(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.books, file, indent=4)

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

        print(f"book '{book['title']}' added")
    
    def get_book_status(self):
        print('\n'.join([f'{key} - {value}' for key, value in BOOK_STATUSES.items()]))
        return BOOK_STATUSES.get(input('status: '), 'not specified')

    def list_books(self):
        if not self.books:
            return 'no books to display'                

    def remove_book(self):
        if not self.books:
            print('no books to remove')
            return

        print('books in library:')
        for i, book in enumerate(self.books, start=1):
            print(f"{i}. {book['title']} by {book['author']}")

        title = input('enter book title to delete:\ntitle: ')

        new_books = [book for book in self.books if book.get('title') != title]

        if len(new_books) < len(self.books):
            self.books = new_books
            self.save_books()
            print(f"removed book: {title}")
        else:
            print('book not found')        

def main():
    lib = Library('books_data.json')
    
    while lib.end != 'e':
        print('menu:')
        for key, value in MENU_OPTIONS.items():
            print(f'{key} - {value}')
        choice = input('choose an option: ').lower()
    

if __name__ == '__main__':
    main()

# TODO
# date when book was completed/started
# possibility to rate a book
# ability to modify book status
# ability to modify any of book properties 
# make GUI 
# add SQL database 
# connect to google books API to fetch covers/info
# user should pick from fetched books or add his custom one
