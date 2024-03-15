-- List records with names and scores (excluding rows with NULL name) ordered by descending score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
