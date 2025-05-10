import json, os

class Library:

    def __init__(self):
        self.books = []
        self.args = ['title', 'author', 'pages', 'status']
        self.file_name = 'books_data.json'

        # create file if one doesn't exist, then load book data
        if not os.path.exists(self.file_name):
            with open(self.file_name, 'w') as file:
                json.dump([], file)

        self.load_books_data()
        self.end = ''
                
        self.clear_cli()

    def clear_cli(self):
        if os.name == 'nt':
            os.system('cls')
        else: 
            os.system('clear')

    # load file contents and store them in a book list 
    def load_books_data(self):
        if os.path.getsize(self.file_name) > 0:
            with open(self.file_name, 'r') as file:
                data = json.load(file)
                self.books.extend(data)
    
    # determinate which metod user selected
    def method_used(self, x):
        self.clear_cli()
        match x:
            case 'a':
                print('add your book')
                self.add_book()
            case 'l':
                self.list_books()
            case 'r':
                self.remove_book()
            case 'e':
                self.end = 'e'
    
    # adding books to the JSON file and list of books
    def add_book(self):
        book = {}
        for key in self.args:
            if not key == 'status':
                data = input(f'{key}: ')
            else:
                data = self.get_book_status()
                self.clear_cli()
                print(f'book {book['title']} added')

            book[key] = data
        self.books.append(book)

        with open(self.file_name, 'w') as file:
            json.dump(self.books, file, indent=4)
     
    def get_book_status(self):
        self.clear_cli()
        print(
                'w - want to read\n'
                'r - currently reading\n'
                'c - completed\n'
            )

        status = input('status: ')
        match status:
            case 'w':
                return 'want to read'
            case 'r':
                return 'reading'
            case 'c':
                return 'completed'
            case _:
                return 'not specified'

    # list all books
    def list_books(self):
        if not self.books:
            print('no books to display')
            return
        
        for item in self.books:
            print(json.dumps(item, indent = 4))
        
        input('press enter to exit')
        self.clear_cli()

    # removing book from file
    def remove_book(self):
        if not self.books:
            print('no books to remove')
            return

        print('books in library: ')
        for i, book in enumerate(self.books, 1):
            print(f'{i}. {book['title']} by {book['author']}')    

        key = input('enter book title to delete\ntitle: ')

        new_books = [book for book in self.books if book.get('title') != key]
        
        if len(new_books) < len(self.books):
            self.books = new_books
            with open(self.file_name, 'w') as file:
                json.dump(self.books, file, indent=4)
            self.clear_cli()
            print(f'removed book: {key}')
        else:
            print('book not found')
          
def main():
    lib = Library()

    while lib.end != 'e':
        choice = input(
            'a - add book\n'
            'l - list all books\n'
            'r - remove book\n'
            'e - exit\n'
        ).lower()
        lib.method_used(choice)

        

main()

# TODO
# remove book from list and file
# text formatting
