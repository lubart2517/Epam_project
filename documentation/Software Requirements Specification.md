Library
Vision
“Library” is web-application which allows librarians to record information about books, authors, users and the book
orders. For library users app allows see info about books and authors and order and return book to library.
Application should provide:
• Storing book orders, users, books and authors in a database;
• Display list of books;
• Updating the list of orders (adding, editing, removing);
• Display list of users;
• Updating the list of users (adding, editing, removing);
• Display list of authors;
• Updating the list of authors (adding, editing, removing);
• Display number of the orders for books and users;
• Filtering by different criteria for orders and users;
1. Orders
1.1 Display list of orders
The mode is designed to view the list of orders, if it possible to display the number of orders for a specified
period of time and also display users which don’t returned books at time.
Main scenario:
• User selects item “Orders”;
• Application displays list of Orders.
Pic. 1.1 View the Orders list.
The list displays the following columns:
• User name;
• Book title;
• Add date – date of adding order;
• Order time – rental time in days, minimal time is one day;
Filtering by date:
• In the order list view mode, the user sets a date filter and presses the refresh list button (to the
right of the date entry field);
• The application will display a form to view the list of orders with updated data.




2. Authors
2.1 Display list of authors
This mode is intended for viewing and editing the authors list
Main scenario:
• User selects item “Authors”;
• Application displays list of authors.
Pic. 2.1 View the authors list.
The list displays the following columns:
• Author name – author name;

2.2 Add author  (available only for librarians)
Main scenario:
• User clicks the “Add” button in the authors list view mode;
• Application displays form to enter author data;
• User enters author data and presses “Add author” button;
• If any data is entered incorrectly, incorrect data messages are displayed;
• If entered data is valid, then record is adding to database;
• If error occurs, then error message is displaying;
• If new author record is successfully added, then list of authors with added records is displaying.
Cancel operation scenario:
• User clicks the “Add” button in the authors list view mode;
• Application displays form to enter author data;
• User enters author data and presses “Cancel” button;
• Data don’t save in data base, then list of authors records is displaying to user.
Pic. 2.2 Add author
When adding an author, the following details are entered:
• Author name – author name;
• Author surname – author surname;
• Author patronymic – author patronymic;
Constraints for data validation:
• Author name – author name;
• Author surname – author surname;
• Author patronymic – author patronymic;

2.3 Edit author  (available only for librarians)
Main scenario:
• User clicks the “Edit” button in the books list view mode;
• Application displays form to enter book data;
• User enters book data and presses “Save” button;
• If any data is entered incorrectly, incorrect data messages are displayed;
• If entered data is valid, then edited data is added to database;
• If error occurs, then error message is displaying;
• If book record is successfully edited, then list of books with added records is displaying.
Cancel operation scenario:
• User clicks the “Edit” button in the books list view mode;
• Application displays form to enter book data;
• User enters book data and presses “Cancel” button;
• Data don’t save in data base, then list of books records is displaying to user.
Pic. 3.3 Edit book.
2.4 Removing the author (available only for librarians)
Main scenario:
• The user, while in the list of authors mode, presses the "Delete" button in the selected author line;
• Application displays confirmation dialog “Please confirm delete author?”;
• The user confirms the removal of the author;
• Record is deleted from database;
• If error occurs, then error message displays;
• If book record is successfully deleted, then list of authors without deleted records is displaying.
Cancel operation scenario:
• User is in display mode of authors list and press “Delete” button;
• Application displays confirmation dialog “Please confirm delete author?”;
• User press “Cancel” button;
• List of authors without changes is displaying.
Pic. 3.4 Delete author dialog.





3. Books
3.1 Display list of books
This mode is intended for viewing and editing the books list
Main scenario:
• User selects item “Books”;
• Application displays list of books.
Pic. 3.1 View the books list.
The list displays the following columns:
• Book title – book’s title;
• Book description – book’s description;
• Number of books in library.
Filtering by author:
• In the books list view mode, the user sets an author id  filter and presses the refresh list button (to the
right of the find entry field);
• The application will display a form to view the list of books with updated data.
Filtering by count:
• In the books list view mode, the user sets a count  filter and presses the refresh list button (to the
right of the find entry field);
• The application will display a form to view the list of books with updated data.
Filtering by name:
• In the books list view mode, the user sets a name_contains
filter and presses the refresh list button (to the right of the find entry field);
• The application will display a form to view the list of books with updated data.

3.2 Add book (available only for librarians)
Main scenario:
• User clicks the “Add” button in the books list view mode;
• Application displays form to enter book data;
• User enters car data and presses “Add book” button;
• If any data is entered incorrectly, incorrect data messages are displayed;
• If entered data is valid, then record is adding to database;
• If error occurs, then error message is displaying;
• If new book record is successfully added, then list of books with added records is displaying.
Cancel operation scenario:
• User clicks the “Add” button in the books list view mode;
• Application displays form to enter book data;
• User enters book data and presses “Cancel” button;
• Data don’t save in data base, then list of books records is displaying to user.
Pic. 3.2 Add book
When adding a book, the following details are entered:
• Book name – book name;
• Book description – book description;
• Count  – count of books in the library;
• Author  – book author;
Constraints for data validation:
• Book name – maximum length of 30 characters;
• Book description – maximum length of 90 characters;
• Count  – 0<=count<=100;
• Author  – book author;

3.3 Edit book (available only for librarians)
Main scenario:
• User clicks the “Edit” button in the books list view mode;
• Application displays form to enter book data;
• User enters book data and presses “Save” button;
• If any data is entered incorrectly, incorrect data messages are displayed;
• If entered data is valid, then edited data is added to database;
• If error occurs, then error message is displaying;
• If book record is successfully edited, then list of books with added records is displaying.
Cancel operation scenario:
• User clicks the “Edit” button in the books list view mode;
• Application displays form to enter book data;
• User enters book data and presses “Cancel” button;
• Data don’t save in data base, then list of books records is displaying to user.
Pic. 3.3 Edit book.
3.4 Removing the book (available only for librarians)
Main scenario:
• The user, while in the list of books mode, presses the "Delete" button in the selected book line;
• Application displays confirmation dialog “Please confirm delete book?”;
• The user confirms the removal of the book;
• Record is deleted from database;
• If error occurs, then error message displays;
• If book record is successfully deleted, then list of books without deleted records is displaying.
Cancel operation scenario:
• User is in display mode of books list and press “Delete” button;
• Application displays confirmation dialog “Please confirm delete book?”;
• User press “Cancel” button;
• List of books without changes is displaying.
Pic. 3.4 Delete book dialog.

3.5 Add order
Main scenario:
• User clicks the “Order” button in the book detail view mode;
• Application displays form to enter order data;
• User enters order data and presses “Save” button;
• If any data is entered incorrectly, incorrect data messages are displayed;
• If entered data is valid, then record is adding to database;
• If error occurs, then error message is displaying;
• If new order record is successfully added, then list of orders of the user with added record is displaying.
Cancel operation scenario:
• User clicks the “Add” button in the order list view mode;
• Application displays form to enter order data;
• User enters order data and presses “Cancel” button;
• Data don’t save in data base, then list of orders of the user is displaying to user.
Pic. 1.2 Add order.
When adding a order, the following details are entered:
• Ordering time – ordering time in days, minimal time is one day.
