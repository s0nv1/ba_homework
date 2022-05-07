class Author:
    def __init__(self, name, country, birthday):
        self.name = name  
        self.country = country
        self.birthday = birthday
        self.books = []
    
    
    def __str__(self):
        info = f'***Author***\n{self.name}\n'
        for book in self.books:
            info += f'{book.name}:{book.year}\n'
        return info
    
    def __repr__(self):
        return self.name 

class Book:
    
    amount = 0
    
    def __init__(self, name, year, author):
        self.name = name 
        self.year = year 
        self.author = author # instance class author
    
    def __len__(self):
        return amount
    
    def __str__(self):
        return f'{self.name} {self.year}'
    
    def __repr__(self):
        return self.name

class Library:
    def __init__(self, name):
        self.name = name 
        self.books = []
        self.authors = []
    
    def new_book(self, name, year, author):
        new_book = Book(name, year, author)
        new_book.amount += 1
        author.books.append(new_book)
        self.books.append(new_book)
        if author not in self.authors:
            self.authors.append(author)
        return new_book
        
    def group_by_author(self, author):
        return author.books
    
    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]
    
    def __repr__(self):
        return self.name
    
    def __str__(self):
        info = f'---{self.name}---\n'
        for author in self.authors:
            info += f'Name: {author.name}\n Country:{author.country}\n Birthday:{author.birthday}\n'
            for book in autor.books:
                info += f'Name: {book.name}, year:{book.year}\n'
        return f'{self.name}'

lib = Library('UkrBooks')
shewchenko = Author('Shevchenko', 'Ukraine', 1814)
valk = Author('Valk', 'Germany', 1980)
lib.new_book('Kobzar', 1840, shewchenko)
lib.new_book('Son', 1865, shewchenko)
lib.new_book('Katerina', 1840, shewchenko)
lib.new_book('Misuta', 2020, valk)
lib.new_book('Saga', 2019, valk)

print(lib.group_by_author(shewchenko))
print(lib.group_by_year(1840))
for i in lib.authors:
    print(i.name)

