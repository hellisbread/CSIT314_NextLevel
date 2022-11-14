CREATE TABLE [IF NOT EXISTS] author (
	users_ptr_id INTEGER PRIMARY KEY,
	name VARCHAR(255) NOT NULL,
	status VARCHAR(1) NOT NULL,
	FOREIGN KEY (users_ptr_id)
		REFERENCES user(id)
		ON DELETE CASCADE
		ON UPDATE NO ACTION
);

INSERT INTO author(users_ptr_id, name, status) 
VALUES
(1, “name1”, “0”), 
(2, “name2”, “0”), 
(3, “name3”, “0”), 
(4, “name4”, “0”), 
(5, “name5”, “0”), 
(6, “name6”, “0”), 
(7, “name7”, “0”), 
(8, “name8”, “0”), 
(9, “name9”, “0”), 
(10, “name10”, “0”), 
(11, “name11”, “0”), 
(12, “name12”, “0”), 
(13, “name13”, “0”), 
(14, “name14”, “0”), 
(15, “name15”, “0”), 
(16, “name16”, “0”), 
(17, “name17”, “0”), 
(18, “name18”, “0”), 
(19, “name19”, “0”), 
(20, “name20”, “0”), 
(21, “name21”, “0”), 
(22, “name22”, “0”), 
(23, “name23”, “0”), 
(24, “name24”, “0”), 
(25, “name25”, “0”);
