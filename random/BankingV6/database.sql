CREATE DATABASE banking;

USE banking;

CREATE TABLE bankacc (
    id INT AUTO_INCREMENT PRIMARY KEY,
    balance DECIMAL(10, 2) NOT NULL
);

--Test
--INSERT INTO bankacc (balance) VALUES (100.50);
