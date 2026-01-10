USE library_management_system;

INSERT INTO books (title, author, category, total_copies, available_copies) VALUES
('Harry Potter and the Sorcerer\'s Stone', 'J.K. Rowling', 'Fantasy', 10, 8),
('The Great Gatsby', 'F. Scott Fitzgerald', 'Classic', 5, 4),
('To Kill a Mockingbird', 'Harper Lee', 'Fiction', 7, 7),
('1984', 'George Orwell', 'Dystopian', 6, 5),
('Python for Beginners', 'Mark Lutz', 'Technology', 3, 3);

INSERT INTO members (name, email, join_date, status) VALUES
('Amit Sharma', 'amit@gmail.com', '2024-02-15', 'active'),
('Riya Patel', 'riya@gmail.com', '2024-03-20', 'active'),
('Neha Singh', 'neha@gmail.com', '2024-04-10', 'active'),
('Karan Mehta', 'karan@gmail.com', '2024-04-25', 'inactive');

INSERT INTO book_issues (book_id, member_id, issue_date, due_date, return_date) VALUES
(1, 1, '2024-04-01', '2024-04-15', '2024-04-10'),
(2, 2, '2024-04-05', '2024-04-20', NULL),
(4, 3, '2024-04-10', '2024-04-25', '2024-04-22');
