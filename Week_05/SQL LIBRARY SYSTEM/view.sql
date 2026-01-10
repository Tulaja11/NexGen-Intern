USE library_management_system;

CREATE VIEW issued_books_view AS
SELECT m.name AS Member, b.title AS Book, i.issue_date, i.due_date, i.return_date
FROM book_issues i
JOIN books b ON i.book_id = b.book_id
JOIN members m ON i.member_id = m.member_id;

SELECT * FROM issued_books_view;
