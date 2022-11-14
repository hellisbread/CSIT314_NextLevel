CREATE TABLE [IF NOT EXISTS] reviewer (
	users_ptr_id INTEGER PRIMARY KEY,
	maxPaper INTEGER DEFAULT 0,
	name VARCHAR(255) NOT NULL,
	status VARCHAR(1) NOT NULL,
	FOREIGN KEY (users_ptr_id)
		REFERENCES user(id)
		ON DELETE CASCADE
		ON UPDATE NO ACTION
);

INSERT INTO reviewer (users_ptr_id, maxPaper, name, status) 
VALUES
(26, 1, “name26”, “0”),
(27, 2, “name27”, “0”),
(28, 1, “name28”, “0”),
(29, 3, “name29”, “0”),
(30, 1, “name30”, “0”),
(31, 4, “name31”, “0”),
(32, 1, “name32”, “0”),
(33, 5, “name33”, “0”),
(34, 1, “name34”, “0”),
(35, 3, “name35”, “0”),
(36, 1, “name36”, “0”),
(37, 4, “name37”, “0”),
(38, 1, “name38”, “0”),
(39, 2, “name39”, “0”),
(40, 1, “name40”, “0”),
(41, 1, “name41”, “0”),
(42, 1, “name42”, “0”),
(43, 2, “name43”, “0”),
(44, 1, “name44”, “0”),
(45, 1, “name45”, “0”),
(46, 3, “name46”, “0”),
(47, 1, “name47”, “0”),
(48, 1, “name48”, “0”),
(49, 2, “name49”, “0”),
(50, 1, “name50”, “0”);
