
-- Drop existing tables in dependency order
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS menu_items;
DROP TABLE IF EXISTS users;

-- Staff users
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    role TEXT NOT NULL DEFAULT 'staff'
);

-- Café menu items
CREATE TABLE menu_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    description TEXT,
    price_cents INTEGER NOT NULL,
    available INTEGER NOT NULL DEFAULT 1
);

-- Customer orders
CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    customer_name TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'Pending',
    notes TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Items belonging to each order
CREATE TABLE order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    menu_item_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (menu_item_id) REFERENCES menu_items(id)
);

-- Seed menu items
INSERT INTO menu_items (name, category, description, price_cents, available)
VALUES
('Café con Leche', 'Drinks', 'Traditional Cuban coffee with steamed milk.', 350, 1),
('Cuban Sandwich', 'Food', 'Roasted pork, ham, Swiss cheese, pickles, and mustard.', 850, 1),
('Guava Pastelito', 'Pastries', 'Flaky pastry filled with sweet guava.', 250, 1),
('Cuban Toast', 'Food', 'Fresh Cuban bread toasted with butter.', 200, 1),
('Cortadito', 'Drinks', 'Strong Cuban espresso with steamed milk.', 275, 1),
('Ham Croqueta', 'Food', 'Traditional Cuban ham croquette.', 175, 1);

-- Seed customer orders
INSERT INTO orders (customer_name, status, notes)
VALUES
('Alex Rodriguez', 'Preparing', 'Extra napkins'),
('Maria Lopez', 'Pending', 'No special requests'),
('David Perez', 'Ready', 'Takeout order');

-- Seed order items
INSERT INTO order_items (order_id, menu_item_id, quantity)
VALUES
(1, 2, 1),
(1, 1, 1),
(2, 4, 2),
(2, 1, 1),
(3, 3, 3),
(3, 5, 2);
