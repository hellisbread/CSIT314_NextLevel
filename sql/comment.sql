CREATE TABLE [IF NOT EXISTS] comment (
	id INTEGER PRIMARY KEY,
	commenter VARCHAR(255),
	rating INTEGER,
	description VARCHAR(255),
	review_id INTEGER,
	FOREIGN KEY (reviewer_id)
		REFERENCES reviewer(id)
		ON DELETE CASCADE
		ON UPDATE NO ACTION
);


INSERT INTO comment (id, commenter, rating, description, reviewer_id) VALUES 
(1, “reviewer 27”, 3, “description1”, 27),
(2, “reviewer 40”, 2, “description2”, 40),
(3, “reviewer 29”, 2, “description3”, 29),
(4, “reviewer 30”, 3, “description4”, 30);
