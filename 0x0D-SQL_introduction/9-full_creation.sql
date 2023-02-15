-- creates a table second_table in the database 
--  in your MySQL server and add multiples rows
CREATE TABLE IF NOT EXISTS second_table (id INT AUTOINCREMENT, name VARCHAR(256), score INT);
INSERT INTO second_table (name=?, score=?) VALUES ("John", 10);
INSERT INTO second_table (name=?, score=?) VALUES ("Alex", 3);
INSERT INTO second_table (name=?, score=?) VALUES ("Bob", 14);
INSERT INTO second_table (name=?, score=?) VALUES ("George", 8);
