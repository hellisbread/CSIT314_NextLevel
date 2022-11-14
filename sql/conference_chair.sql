CREATE TABLE [IF NOT EXISTS] conference_chair (
	users_ptr_id INTEGER PRIMARY KEY,
	name VARCHAR(255) NOT NULL,
	status VARCHAR(1) NOT NULL,
	FOREIGN KEY (users_ptr_id)
		REFERENCES user(id)
		ON DELETE CASCADE
		ON UPDATE NO ACTION
);

INSERT INTO conference_chair (users_ptr_id, name, status) 
VALUES
(51, “name51”, “0”), 
(52, “name52”, “0”), 
(53, “name53”, “0”), 
(54, “name54”, “0”), 
(55, “name55”, “0”), 
(56, “name56”, “0”), 
(57, “name57”, “0”), 
(58, “name58”, “0”), 
(59, “name59”, “0”), 
(60, “name60”, “0”), 
(61, “name61”, “0”), 
(62, “name62”, “0”), 
(63, “name63”, “0”), 
(64, “name64”, “0”), 
(65, “name65”, “0”), 
(66, “name66”, “0”), 
(67, “name67”, “0”), 
(68, “name68”, “0”), 
(69, “name69”, “0”), 
(70, “name70”, “0”), 
(71, “name71”, “0”), 
(72, “name72”, “0”), 
(73, “name73”, “0”), 
(74, “name74”, “0”), 
(75, “name75”, “0”);
