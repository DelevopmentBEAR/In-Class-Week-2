class Author:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    # adds a book title to the author's list of published books
    def publish(self, title):
        self.books.append(title)
        
    # def __str__(self):
    #     # checks if the author has published any books and returns a string representation of the author and their published books
    #     if self.books:
    #         books_list = ', '.join(self.books)
    #         return f'{self.name}, Books Published: {books_list}'
    #     # else, if the author has not published any books, returns a string representation of the author with a message indicating that no books have been published
    #     else:
    #         return f'{self.name}, No Books Published'
    
    # ^ Same as above, but using a more concise approach with the 'or' operator to handle the case where the author has not published any books
    def __str__(self):
        book_list = ', '.join(self.books) or 'No Books Published'
        return f'{self.name}, Books Published: {book_list}'

# defines a main function that creates an Author object, publishes some books, and prints the author's information
def main():
    Shakespeare = Author('William Shakespeare')
    Shakespeare.publish('Hamlet')
    Shakespeare.publish('Romeo and Juliet')

    print(Shakespeare) # <- prints 'William Shakespeare, Books Published: Hamlet, Romeo and Juliet'

    Clara = Author('Clara')
    print(Clara) # <- prints 'Clara, No Books Published'    
    
main()