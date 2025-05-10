import json, os

class Library:

    def __init__(self):
        self.books = []
        self.args = ['title', 'author', 'pages', 'status']
        self.file_name = 'books_data.json'

        # create file if one doesn't exist, then load book data
        if not os.path.exists(self.file_name):
            with open(self.file_name, 'w') as file:
                data = json.write(file)

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
            json.dump(self.books, file, indent = 4)
     
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
                return ''

    # determinate which metod user selected
    def method_used(self, x):
        self.clear_cli()
        match x:
            case 'a':
                print('add your book')
                self.add_book()
            case 'l':
                for item in self.books:
                    print(json.dumps(item, indent = 4))
                
                input('press enter to exit')
                self.clear_cli()
            case 'r':
                """ remove book """
            case 'e':
                self.end = 'e'
          
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
