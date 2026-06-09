CREATE TABLE users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(255),
    balance DECIMAL(10,2)
);

CREATE TABLE transactions(
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    amount DECIMAL(10,2),
    transaction_type VARCHAR(20)
);

CREATE TABLE loans(
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    loan_amount DECIMAL(10,2),
    prediction VARCHAR(20)
);