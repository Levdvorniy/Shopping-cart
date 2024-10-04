CREATE TABLE users (
    user_id INT PRIMARY KEY,
    user_name VARCHAR(255)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(255),
	price INT
);

INSERT INTO Users(user_id, user_name)
Values
(1, 'Terminator T-1000');
INSERT INTO Users(user_id, user_name)
Values
(2, 'David Bowie');
INSERT INTO Users(user_id, user_name)
Values
(3, 'Killmister');
INSERT INTO Users(user_id, user_name)
Values
(4, 'John Doe');

INSERT INTO products(product_id, product_name, price)
Values
(1, 'Мотоцикл', 0);
INSERT INTO products(product_id, product_name, price)
Values
(2, 'Пулемёт Гатлинг', 0);
INSERT INTO products(product_id, product_name, price)
Values
(3, 'Микрофон', 0);
INSERT INTO products(product_id, product_name, price)
Values
(4, 'Виски', 0);

CREATE TABLE cart_items(
	cart_id INT,
    user_id INT,
    product_id INT,
    Quantity INT,
	PRIMARY KEY (user_id, product_id),
	FOREIGN KEY (user_id) REFERENCES users(user_id),
	FOREIGN KEY (product_id) REFERENCES products(product_id)
);