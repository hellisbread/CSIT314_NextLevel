
CREATE TABLE IF NOT EXISTS "user" 
("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"email" varchar(255) NOT NULL UNIQUE, 
"username" varchar(255) NOT NULL UNIQUE, 
"password" varchar(255) NOT NULL);

CREATE TABLE IF NOT EXISTS "author" ("users_ptr_id" bigint NOT NULL PRIMARY KEY REFERENCES "user" ("id") DEFERRABLE INITIALLY DEFERRED, "name" varchar(255) NOT NULL, "status" varchar(1) NOT NULL);

CREATE TABLE IF NOT EXISTS "conference_chair" ("users_ptr_id" bigint NOT NULL PRIMARY KEY REFERENCES "user" ("id") DEFERRABLE INITIALLY DEFERRED, "name" varchar(255) NOT NULL, "status" varchar(1) NOT NULL);

CREATE TABLE IF NOT EXISTS "reviewer" ("users_ptr_id" bigint NOT NULL PRIMARY KEY REFERENCES "user" ("id") DEFERRABLE INITIALLY DEFERRED, "maxPaper" integer NOT NULL, "name" varchar(255) NOT NULL, "status" varchar(1) NOT NULL);

CREATE TABLE IF NOT EXISTS "system_admin" ("users_ptr_id" bigint NOT NULL PRIMARY KEY REFERENCES "user" ("id") DEFERRABLE INITIALLY DEFERRED, "status" varchar(1) NOT NULL);

CREATE TABLE IF NOT EXISTS "review" 
("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"rating" integer NOT NULL, 
"title" varchar(255) NOT NULL, 
"description" text NOT NULL, 
"paper_id" bigint NOT NULL REFERENCES 
"paper" ("id") DEFERRABLE INITIALLY DEFERRED, 
"reviewer_id" bigint NOT NULL REFERENCES 
"reviewer" ("users_ptr_id") DEFERRABLE INITIALLY DEFERRED);

CREATE TABLE IF NOT EXISTS "paper" 
("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"topic" varchar(255) NOT NULL, 
"description" varchar(255) NOT NULL, 
"submitted_date" datetime NOT NULL, 
"fileName" varchar(255) NOT NULL, 
"saved_file" varchar(100) NOT NULL, 
"uploaded_by" varchar(255) NOT NULL, 
"status" varchar(255) NOT NULL);

CREATE TABLE IF NOT EXISTS "paper_authors" 
("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"paper_id" bigint NOT NULL REFERENCES 
"paper" ("id") DEFERRABLE INITIALLY DEFERRED, 
"author_id" bigint NOT NULL REFERENCES 
"author" ("users_ptr_id") DEFERRABLE INITIALLY DEFERRED);

CREATE TABLE IF NOT EXISTS "bidded_paper" 
("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"bid_date" datetime NOT NULL, 
"submission_date" datetime NULL, 
"status" varchar(255) NOT NULL, 
"paper_id" bigint NOT NULL REFERENCES 
"paper" ("id") DEFERRABLE INITIALLY DEFERRED, 
"reviewer_id" bigint NOT NULL REFERENCES 
"reviewer" ("users_ptr_id") DEFERRABLE INITIALLY DEFERRED);


CREATE TABLE IF NOT EXISTS "review_rating" 
("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"rating" integer NOT NULL, 
"author_id" bigint NOT NULL REFERENCES 
"author" ("users_ptr_id") DEFERRABLE INITIALLY DEFERRED, 
"paper_id" bigint NOT NULL REFERENCES 
"paper" ("id") DEFERRABLE INITIALLY DEFERRED, 
"reviewer_id" bigint NOT NULL REFERENCES 
"reviewer" ("users_ptr_id") DEFERRABLE INITIALLY DEFERRED, 
"review_id" bigint NOT NULL REFERENCES 
"review" ("id") DEFERRABLE INITIALLY DEFERRED);

CREATE TABLE IF NOT EXISTS "comment" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "commenter" varchar(255) NOT NULL, "rating" integer NOT NULL, "description" text NOT NULL, "review_id" bigint NOT NULL REFERENCES "review" ("id") DEFERRABLE INITIALLY DEFERRED, "sent_date" datetime NOT NULL);




