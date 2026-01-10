USE library_management_system;

INSERT INTO books (title, author, category, total_copies, available_copies)
VALUES ('Database Systems', 'Elmasri & Navathe', 'Education', 4, 4);

SELECT * FROM books;

UPDATE books
SET available_copies = available_copies - 1
WHERE book_id = 2;

SELECT * FROM books;

DELETE FROM books 
WHERE book_id = 3;

START TRANSACTION;

UPDATE books
SET available_copies = available_copies - 1
WHERE book_id = 3 AND available_copies > 0;

COMMIT;

SELECT * FROM books;