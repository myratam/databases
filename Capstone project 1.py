import sqlite3

#Connect to the database
db = sqlite3.connect('data/ebookstore_db')

#Get a cursor object
cursor = db.cursor() 

#Create a table called books
cursor.execute('''
    CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT, author TEXT, qty INTEGER)
''')
db.commit()

#### Adding rows to the table ####

#User 1
id1 = 3001
title1 = 'A Tale of Two Cities'
author1 = 'Charles Dickens'
qty1 = 30

#User 2
id2 = 3002
title2 = 'Harry Potter and the Philosopher\'s Stone'
author2 = 'J.K. Rowling'
qty2 = 40

#User 3
id3 = 3003
title3 = 'The Lion, the Witch and the Wardrobe'
author3 = 'C.S. Lewis'
qty3 = 25

#User 4
id4 = 3004
title4 = 'The Lord of the Rings'
author4 = 'J.R.R Tolkien'
qty4 = 37

#User 5
id5 = 3005
title5 = 'Alice in Wonderland'
author5 = 'Lewis Carroll'
qty5 = 12

#Insert user 1
cursor.execute('''INSERT INTO books(id, title, author, qty)
                  VALUES(?,?,?,?)''', (id1, title1, author1, qty1))
print('Author inserted')

#Insert user 2
cursor.execute('''INSERT INTO books(id, title, author, qty)
                  VALUES(?,?,?,?)''', (id2, title2, author2, qty2))
print('Author inserted')

#Insert user 3
cursor.execute('''INSERT INTO books(id, title, author, qty)
                  VALUES(?,?,?,?)''', (id3, title3, author3, qty3))
print('Author inserted')

#Insert user 4
cursor.execute('''INSERT INTO books(id, title, author, qty)
                  VALUES(?,?,?,?)''', (id4, title4, author4, qty4))
print('Author inserted')

#Insert user 5
cursor.execute('''INSERT INTO books(id, title, author, qty)
                  VALUES(?,?,?,?)''', (id5, title5, author5, qty5))
print('Author inserted')

db.commit()


#### Functions ####

#Define the functions for add book
def add_book():
    id = input("Enter the book ID: ")
    title = input("Enter the book title: ")
    author = input("Enter the author name: ")
    qty = int(input("Enter the quantity available: "))

    #Insert book
    cursor.execute('''INSERT INTO books (id, title, author, qty) 
                   VALUES (?, ?, ?,?)''', (id, title, author, qty))  
    print('Book added successfully')
    db.commit()

#Define the functions for update book
def update_book():
    id = int(input("Enter the book ID to update: "))
    new_qty = int(input("Enter the new quantity available: "))

    #Update book
    cursor.execute("UPDATE books SET Qty=? WHERE id=?", (new_qty, id))
    print('Book updated successfully')
    db.commit()

#Define the functions for delete book
def delete_book():
    id = int(input("Enter the book ID to delete: "))
    cursor.execute("DELETE FROM books WHERE id=?", (id,))
    print('Book deleted successfully')
    db.commit()
    
#Define the functions for search books
def search_books():
    search_term = input("Enter a search term (title or author): ")
    cursor.execute('''SELECT * FROM books WHERE Title LIKE ? OR Author LIKE ?''', 
                   ('%' + search_term + '%', '%' + search_term + '%'))

    #Retrieving data
    results = cursor.fetchall()
    if len(results) == 0:
        print('No books found')
    else:
        print('Search results:')
        for row in results:
            print(row)

#Define the function for exit
def exit():
    db.close
    print('Connection to database closed')


#### Main menu loop ####
while True:
    # Print the menu options
    print("1. Enter book")
    print("2. Update book")
    print("3. Delete book")
    print("4. Search books")
    print("0. Exit")
    
    #Get the user's choice
    choice = input("Enter your choice: ")
    
    #Call the function based on the user's choice
    if choice == '1':
        add_book()
    elif choice == '2':
        update_book()
    elif choice == '3':
        delete_book()
    elif choice == '4':
        search_books()
    elif choice == '0':
        exit() 
    else:
        print("Invalid choice")

