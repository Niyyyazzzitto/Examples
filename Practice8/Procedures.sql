--procedure 1
CREATE OR REPLACE PROCEDURE inserting_name_phone(
    p_name TEXT,
    p_address VARCHAR(255),
    p_number VARCHAR(255)
)
LANGUAGE plpgsql
AS $$
DECLARE 
   usersr BOOLEAN;
BEGIN
   SELECT EXISTS(
       SELECT 1 FROM phonebook
       WHERE name = p_name AND address = p_address
   ) INTO usersr;
   IF usersr THEN
       UPDATE phonebook
       SET number = p_number
       WHERE name = p_name AND address = p_address;
   ELSE
       INSERT INTO phonebook (name, address, number)
       VALUES (p_name, p_address, p_number);
   END IF;
END;
$$; 

--procedure 2
CREATE OR REPLACE PROCEDURE loop_using_proc(
    p_names TEXT[],
    p_numbers VARCHAR(255)[]
)
LANGUAGE plpgsql
AS 
$$
DECLARE
    i INT;
    current_name TEXT;
    current_phone VARCHAR(255);
BEGIN
    FOR i IN 1..array_length(p_names, 1) LOOP
        current_name := p_names[i];
        current_phone := p_numbers[i];
        IF length(current_phone) < 10 THEN
            RAISE NOTICE 'Not a proper number!';
        ELSE
            INSERT INTO phonebook(name, number) VALUES (current_name, current_phone);
        END IF;
    END LOOP;
END;
$$;

--procedure 3
CREATE OR REPLACE PROCEDURE deleting(p_username TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook 
    WHERE name = p_username; -- Теперь база точно знает, что p_username - это наш ввод
END;
$$;