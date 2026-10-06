
CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL
);

INSERT INTO products (id, name, price, stock) VALUES
(1, 'Laptop',   150000.00, 14),
(2, 'Mouse',    2000.00,   30),
(3, 'Keyboard', 4000.00,   40);
