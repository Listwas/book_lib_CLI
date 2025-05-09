import csv, os

class Library:

    def __init__(self):
        self.books = []
        self.args = ['title', 'author', 'pages', 'status']
        self.file_name = 'books_data.csv'
        self.read_file()
        

    def read_file(self):
        with open(self.file_name, 'r') as csvfile:
            cr = csv.reader(csvfile, delimiter='|')

            for row in cr:
                book = {}
                index = 0    
                for item in self.args:
                    index += 1
                    book[item] = row[index-1]
                self.books.append(book)


    def add_book(self):
        print('\nadd your book')

        book = {}
        for item in self.args:
            book[item] = input(f'{item}: ')

        self.books.append(book)

        # save data to file 
        with open(self.file_name, 'w') as file:
            w = csv.writer(file, delimiter='|')
            w.writerows([x.values() for x in self.books])
        
    def method_used(self, x):
        match x:
            case 'a':
                self.add_book()
            case 'l':
                print(self.books)
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
        ).lower()
        lib.method_used(choice)

        

main()