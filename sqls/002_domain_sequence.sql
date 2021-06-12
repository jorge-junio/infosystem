-- Postgres

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE OR REPLACE FUNCTION domain_seq_nextval(p_domain_id CHAR(32), p_sequence_name VARCHAR(100), p_step NUMERIC(3) DEFAULT 1)
RETURNS BIGINT
LANGUAGE plpgsql
AS $$ DECLARE
  l_domain_seq_value NUMERIC;
BEGIN
  IF p_step <= 0 THEN
    RAISE EXCEPTION 'p_step param must be greater than zero.';
  END IF;
 
  UPDATE domain_sequence
  SET    value = value + COALESCE(p_step, 1, 1, p_step)
  WHERE  p_domain_id = domain_id AND 
         p_sequence_name = name
  RETURNING value INTO l_domain_seq_value;
         
  IF l_domain_seq_value IS NOT NULL THEN
    -- Se houve update o "value" e atualizado e retornado
    RETURN l_domain_seq_value;
  ELSE 
    -- Se nao houve UPDATE nos registros, uma nova sequencia e criada
    -- com "value" e "step" igual p_step e retorna p_step. 
    INSERT
    INTO   domain_sequence(id, domain_id, name, value)
    VALUES (REPLACE(CONCAT(uuid_generate_v4(), ''), '-', ''), p_domain_id, p_sequence_name, p_step);

    RETURN p_step;
  END IF;  
  COMMIT;
END;
$$;