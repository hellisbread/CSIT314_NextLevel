CREATE TABLE [IF NOT EXISTS] review (
	id INTEGER PRIMARY KEY,
	rating INTEGER,
	title VARCHAR(255),
	description VARCHAR(255),
	paper_id INTEGER,
	reviewer_id INTEGER,
	FOREIGN KEY (paper_id)
		REFERENCES paper(id)
		ON DELETE CASCADE
		ON UPDATE NO ACTION,
	FOREIGN KEY (reviewer_id )
		REFERENCES reviewer(id)
		ON DELETE CASCADE
		ON UPDATE NO ACTION
);


INSERT INTO review (id, rating, title, description, paper_id, reviewer_id) VALUES 
(1, -3, “review1”, “description1”, 2, 27),
(2, -2, “review2”, “description2”, 2, 40),
(3, -1, “review3”, “description3”, 4, 29),
(4, 0, “review4”, “description4”, 4, 30),
(5, 3, “review5”, “description5”, 9, 34),
(6, 1, “review6”, “description6”, 11, 36),
(7, -1, “review7”, “description7”, 14, 39),
(8, 1, “review8”, “description8, 16, 41),
(9, 2, “review9”, “description9”, 19, 44),
(10, 1, “review10”, “description10”, 22, 27),
(11, 3, “review11”, “description11”, 24, 29);
