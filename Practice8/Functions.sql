--function 1
CREATE OR REPLACE FUNCTION matching_results(part_of_name TEXT)
RETURNS TABLE(
    out_name VARCHAR(100), 
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
CREATE OR REPLACE FUNCTION pagination(p_limit INT, p_offset INT)
RETURNS TABLE(
    name VARCHAR(100),
    address VARCHAR(255),
    number VARCHAR(255)
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT 
        phonebook.name, 
        phonebook.address, 
        phonebook.number
    FROM phonebook
    LIMIT p_limit OFFSET p_offset;
END;
$$;
