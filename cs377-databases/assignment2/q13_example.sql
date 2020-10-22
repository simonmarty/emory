SET search_path TO artistdb;

-- Let's assume your answer requires two intermediate steps
DROP VIEW IF EXISTS ViewA;
DROP VIEW IF EXISTS ViewB;

-- You create ViewA here to perform the first step
-- ..... --

-- You create ViewB here to perform the first step
-- ..... --

-- You SELECT the results here if it's a question that requires
-- you to report results, or INSERT/UPDATE/DELETE if it requires
-- you to update the database, etc.


-- Now drop the views you created
DROP VIEW IF EXISTS ViewB;
DROP VIEW IF EXISTS ViewA;
