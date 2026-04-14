--function 1
CREATE OR REPLACE FUNCTION matching_results(part_of_name TEXT)
RETURNS TABLE(
    out_name TEXT, 
    out_address VARCHAR(255), 
    out_number VARCHAR(255)
) 
LANGUAGE plpgsql
AS $$
BEGIN 
   RETURN QUERY
   SELECT 
      name,   
      address,
      number  
   FROM phonebook
   WHERE name ILIKE '%' || part_of_name || '%';
END;
$$;

--function 2
CREATE OR REPLACE FUNCTION pagination(limits INT, offset INT)
RETURNS TABLE(
    name TEXT,
    address VARCHAR(255),
    number VARCHAR(255)
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT name, address, number
    FROM phonebook
    LIMIT limits, OFFSET offset;
END;
$$;