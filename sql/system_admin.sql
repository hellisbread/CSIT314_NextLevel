CREATE TABLE [IF NOT EXISTS] system_admin (
	users_ptr_id INTEGER PRIMARY KEY,
	status VARCHAR(1) NOT NULL,
	FOREIGN KEY (users_ptr_id)
		REFERENCES user(id)
		ON DELETE CASCADE
		ON UPDATE NO ACTION
);


INSERT INTO system_admin (users_ptr_id, status) 
VALUES
(76, “0”), 
(77, “0”), 
(78, “0”), 
(79, “0”), 
(80, “0”), 
(81, “0”), 
(82, “0”),
(83, “0”), 
(84, “0”), 
(85, “0”), 
(86, “0”), 
(87, “0”), 
(88, “0”), 
(89, “0”), 
(90, “0”), 
(91, “0”), 
(92, “0”), 
(93, “0”), 
(94, “0”), 
(95, “0”), 
(96, “0”), 
(97, “0”), 
(98, “0”), 
(99, “0”), 
(100, “0”);
