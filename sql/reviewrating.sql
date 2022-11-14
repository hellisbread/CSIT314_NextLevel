CREATE TABLE [IF NOT EXISTS] reviewrating (
	id INTEGER PRIMARY KEY,
	rating INTEGER, 
	author_id INTEGER,
	paper_id INTEGER,
	reviewer_id INTEGER,
	FOREIGN KEY (paper_id)
		REFERENCES paper(id)
		ON DELETE CASCADE
		ON UPDATE NO ACTION,
	FOREIGN KEY (reviewer_id)
		REFERENCES reviewer(id)
		ON DELETE CASCADE
		ON UPDATE NO ACTION,
);

INSERT INTO reviewrating (id, rating, author_id, paper_id, reviewer_id) VALUES 
(1, -1, 3, 2, 27),
(2, 0, 2, 2, 40),
(3, 3, 9, 9, 37),
(4, -1, 3, 2, 27),
(5, 3, 20, 19, 44),
(6, -1, 5, 4, 30),
(7, 2, 12, 11, 36),
(8, 2, 17, 16, 41);
