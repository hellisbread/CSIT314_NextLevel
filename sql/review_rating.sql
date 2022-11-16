CREATE TABLE [IF NOT EXISTS] review_rating (
	id INTEGER PRIMARY KEY,
	rating INTEGER, 
	author_id INTEGER,
	paper_id INTEGER,
	reviewer_id INTEGER,
	review_id INTEGER,
	FOREIGN KEY (paper_id)
		REFERENCES paper(id)
		ON DELETE CASCADE
		ON UPDATE NO ACTION,
	FOREIGN KEY (reviewer_id)
		REFERENCES reviewer(id)
		ON DELETE CASCADE
		ON UPDATE NO ACTION,
	FOREIGN KEY (review_id )
		REFERENCES review(id)
		ON DELETE CASCADE
		ON UPDATE NO ACTION
);


INSERT INTO review_rating (id, rating, author_id, paper_id, reviewer_id, review_id) VALUES 
(1, -1, 2, 2, 27, 1),
(2, 0, 2, 2, 40, 2),
(3, 3, 9, 9, 34, 5),
(4, -1, 3, 2, 27, 1),
(5, 3, 20, 19, 44, 9),
(6, -1, 5, 4, 30, 4),
(7, 2, 12, 11, 36, 6),
(8, 2, 17, 16, 41, 8);

