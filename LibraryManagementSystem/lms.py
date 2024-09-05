import datetime

class lms:
     '''
     LMS Class contains all library functionality (Add, return, borrow, display books)
     '''
     def __init__(self, books, libraryName):
         self.books = 'books.txt'
         self.libraryName = libraryName
         self.bookLib = {}
         id = 1

         with open(self.books) as book:
             bkNames = book.readlines()
         for name in bkNames:
            #print(name)
            self.bookLib.update({str(id):{
             "title":name.replace('\n',''), 'borrower':'', 'date': '', 'status': 'Available'
             }
            })
            id += 1
     def display(self):
         print('-----------------Library of Books-----------------')
         print('Book Id', 'Title')
         print('----------------------------------')
         for key, value in self.bookLib.items():
             print(key,'\t', value.get('title'), '-', value.get('status'))

     def borrow_book(self):
         id = input('Enter book id')
         current_date = datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S')
         if id in self.bookLib.keys():
             if not self.bookLib[id]['status'] == 'Available':
                 print(f'This book is already borrowed by:{self.bookLib[id]['borrower']} on {self.bookLib[id]['date']}')

             elif self.bookLib[id]['status'] == 'Available':
                 name = input('Enter borrower name: ')
                 self.bookLib[id]['borrower'] = name
                 self.bookLib[id]['date'] = current_date
                 self.bookLib[id]['status'] = 'Borrowed'
                 print(f'Book is now borrowed by {name}')
         else:
             print('Book not found in the library')
             return self.borrow_book()

     def add_book(self):
         bookName = input('Enter book name: ')
         if bookName == '':
             print('Book name can’t be empty')
             return self.add_book()
         elif len(bookName) > 25:
             print('Book name is too long. Book name can’t exceed 25 letters')
             return self.add_book()
         else:
             with open(self.books, 'a') as lib:
                 lib.writelines(f'{bookName}\n')

             # Generate a new ID by finding the max existing key and adding 1
             if self.bookLib:
                 new_id = str(int(max(self.bookLib.keys(), key=int)) + 1)
             else:
                 new_id = '1'

             self.bookLib.update({
                 new_id: {
                     'title': bookName,
                     'borrower': '',
                     'date': '',
                     'status': 'Available'
                 }
             })
             print(f'{bookName} is added successfully to the library')

     def return_book(self):
           id = input('Enter book id: ')
           if id in self.bookLib.keys():
               if self.bookLib[id]['status'] == 'Available':
                   print('This book already in the library, book id entered might be incorrect')
               elif self.bookLib[id]['status'] != 'Available':
                    self.bookLib[id]['status'] = 'Available'
                    self.bookLib[id]['borrower'] = ''
                    self.bookLib[id]['date'] = ''
                    print('Book is returned successfully')

           else:
                print('Book id not found in the library')

if __name__ == "__main__":
    try:
        lms = lms('book.txt', 'Book Library')
        choice = {1: 'Display Books', 2: 'Borrow Book', 3: 'Add Books', 4:'Return Books', 5:'Exit Library'}
        exit = False
        while not exit:
            print(f'\n----------Welcome To {lms.libraryName} Library Management System-------\n')
            for key, value in choice.items():
                print('Press', key, 'To', value)
            choice_input = input('Press key: ').lower()
            if choice_input == '1':
                print('\n Displaying Books')
                lms.display()
            elif choice_input == '2':
                print('\n Borrowing Book')
                lms.borrow_book()
            elif choice_input == '3':
                print('\n Adding Book')
                lms.add_book()
            elif choice_input == '4':
                print('\n Returning a Book')
                lms.return_book()
            elif choice_input == 'q':
                exit = True
                break
            else:
                continue
    except Exception as e:
        print('Something went wrong. Please check your input')

    # allBooks = lms('books.txt','Book Library')
    # print(allBooks.display())