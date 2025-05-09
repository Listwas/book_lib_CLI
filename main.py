

class Library:

    def __init__(self):
        self.books = []

    def add_book(self):
        print('\nadd your book')
        args = ['title', 'author', 'pages', 'status']

        book = {}
        for item in args:
            book[item] = input(f'{item}: ')

        self.books.append(book)
        
    def method_used(self, x):
        match x:
            case 'a':
                self.add_book()
            case 'l':
                print(*self.books, sep='\n')
            case 'r':
                """ remove book """


def main():
    end = ''
    lib = Library()

    while end != 'e':
        choice = input(
            'a - add book\n'
            'l - list all books\n'
            'r - remove book\n'
        )
        lib.method_used(choice)

        

main()