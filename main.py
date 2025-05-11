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
    def __init__(self):
        self.books = []
        self.args = ['title', 'author', 'pages', 'status']
        self.file_name = 'books_data.json'
        self.end = ''

        if not os.path.exists(self.file_name):
            with open(self.file_name, 'w') as file:
                json.dump([], file)

        self.load_books_data()
        self.clear_cli()

    def clear_cli(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def load_books_data(self):
        if os.path.getsize(self.file_name) > 0:
            with open(self.file_name, 'r') as file:
                self.books = json.load(file)

    def save_books(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.books, file, indent=4)

    def method_used(self, option):
        self.clear_cli()
        match option:
            case 'a':
                self.add_book()
            case 'l':
                self.list_books()
            case 'r':
                self.remove_book()
            case 'e':
                self.end = 'e'

    def add_book(self):
        print('add your book')
        book = {}        
        for key in self.args:
            if key == 'pages':
                pages = self.get_book_pages(key)
                if pages is None:
                    self.clear_cli()
                    print('too many attempts')    
                    return
                book[key] = pages
            elif key == 'status':
                book[key] = self.get_book_status()
            else:
                book[key] = input(f'{key}: ')

        self.books.append(book)
        self.save_books()

        self.clear_cli()
        print(f"book '{book['title']}' added")

    def get_book_pages(self, key):
        i = 0
        while i < 3:
            try:
                x = int(input(f'{key}: '))
                i = 3
                return x
            except:
                i += 1
                print('value needs to be an integer')
        return None
    
    def get_book_status(self):
        self.clear_cli()
        print('\n'.join([f'{key} - {value}' for key, value in BOOK_STATUSES.items()]))
        return BOOK_STATUSES.get(input('status: '), 'not specified')

    def list_books(self):
        if not self.books:
            print('no books to display')
        else:
            for book in self.books:
                print(json.dumps(book, indent=4))

        input('press Enter to continue...')
        self.clear_cli()

    def remove_book(self):
        if not self.books:
            print('no books to remove')
            return

        print('books in library:')
        for i, book in enumerate(self.books, start=1):
            print(f"{i}. {book['title']} by {book['author']}")

        title = input('enter book title to delete:\ntitle: ')

        new_books = [book for book in self.books if book.get('title') != title]

        self.clear_cli()
        if len(new_books) < len(self.books):
            self.books = new_books
            self.save_books()
            print(f"removed book: {title}")
        else:
            print('book not found')


def main():
    lib = Library()

    while lib.end != 'e':
        print('menu:')
        for key, value in MENU_OPTIONS.items():
            print(f'{key} - {value}')
        choice = input('choose an option: ').lower()
        lib.method_used(choice)


if __name__ == '__main__':
    main()

# TODO
# date when book was completed/started
# possibility to rate a book
# ability to modify book status
# ability to modify any of book properties 
# make GUI (tkinter?)
# add SQL database 
# connect to google books API to fetch covers/info
# user should pick from fetched books or add his custom one
