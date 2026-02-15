CREATE VIEW vw_pokemon_cards AS
SELECT 
    c.id AS card_id,
    c.name AS card_name,
    c.hp,
    c.type,
    c.stage,
    c.info,
    c.damage,
    c.weak,
    c.resist,
    c.retreat,
    c.card_number_in_collection,
    col.id AS collection_id,
    col.collection_set_name,
    col.release_date,
    col.total_cards_collection
FROM tbl_cards c
INNER JOIN tbl_collections col
    ON c.collection_id = col.id;

-- Exemplo de consulta para testar a view:
-- SELECT * FROM vw_pokemon_cards WHERE collection_set_name = 'Base Set';