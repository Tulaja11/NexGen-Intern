USE library_management_system;

SELECT book_id, title, author, category, available_copies
FROM books;

SELECT m.name AS Member, b.title AS Book, i.issue_date, i.due_date
FROM book_issues i
JOIN books b ON i.book_id = b.book_id
JOIN members m ON i.member_id = m.member_id;

SELECT b.title, m.name, i.due_date
FROM book_issues i
JOIN books b ON i.book_id = b.book_id
JOIN members m ON i.member_id = m.member_id
WHERE i.return_date IS NULL AND i.due_date < CURDATE();

SELECT b.title, COUNT(i.issue_id) AS times_borrowed
FROM book_issues i
JOIN books b ON i.book_id = b.book_id
GROUP BY b.title
ORDER BY times_borrowed DESC
LIMIT 5;

SELECT SUM(available_copies) AS total_available_books FROM books;
