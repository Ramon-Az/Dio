-- Seed tbl_collections
INSERT INTO tbl_collections (id, collection_set_name, release_date, total_cards_collection) VALUES
(1, 'Base Set', '1999-01-09', 102),
(2, 'Jungle', '1999-06-16', 64),
(3, 'Fossil', '1999-10-10', 62),
(4, 'Neo Genesis', '2000-12-16', 111),
(5, 'Sword & Shield', '2020-02-07', 202);

-- Seed tbl_cards
INSERT INTO tbl_cards (id, collection_id, hp, name, type, stage, info, damage, weak, resist, retreat, card_number_in_collection) VALUES
(1, 1, 60, 'Pikachu', 'Electric', 'Basic', 'Classic electric mouse; low HP but fast', '30', 'Ground', 'Metal -20', 1, '58/102'),
(2, 1, 120, 'Charizard', 'Fire', 'Stage 2', 'High-attack fire dragon; popular holo', '120', 'Water', NULL, 3, '4/102'),
(3, 2, 70, 'Venusaur', 'Grass', 'Stage 2', 'Powerful grass-type with healing lore', '80', 'Fire', 'Water -30', 3, '15/64'),
(4, 3, 80, 'Gyarados', 'Water', 'Stage 1', 'Aggressive sea serpent; strong attack', '90', 'Electric', NULL, 3, '20/62'),
(5, 4, 60, 'Typhlosion', 'Fire', 'Stage 2', 'Evolves from Cyndaquil; strong flame moves', '90', 'Water', NULL, 2, '33/111'),
(6, 5, 130, 'Zacian V', 'Metal', 'Basic', 'Sword-wielding legendary; V card mechanics', '220', 'Fire', 'Psychic -30', 2, '001/202'),
(7, 5, 90, 'Blastoise', 'Water', 'Stage 2', 'Shell cannon attacks; defensive options', '150', 'Electric', NULL, 4, '009/202'),
(8, 1, 40, 'Clefairy', 'Fairy', 'Basic', 'Cute support card; often used for evolution chains', '20', 'Metal', NULL, 1, '35/102'),
(9, 2, 50, 'Eevee', 'Colorless', 'Basic', 'Many evolutions; versatile in decks', '30', 'Fighting', NULL, 1, '45/64'),
(10, 3, 100, 'Aerodactyl', 'Fighting', 'Basic', 'Fossil-era flyer; strong attack but low retreat', '80', 'Grass', NULL, 1, '12/62'),
(11, 4, 90, 'Mewtwo', 'Psychic', 'Basic', 'High special attack; iconic legendary', '130', 'Psychic', 'Dark -20', 2, '01/111'),
(12, 5, 70, 'Lucario', 'Fighting', 'Stage 1', 'Balanced attacker with special effects', '110', 'Psychic', NULL, 2, '045/202'),
(13, 5, 80, 'Gardevoir', 'Psychic', 'Stage 2', 'Support and control; often used for disruption', '100', 'Dark', NULL, 2, '046/202'),
(14, 1, 160, 'Snorlax', 'Colorless', 'Basic', 'High HP tank; heavy attacks', '180', 'Fighting', NULL, 4, '15/102'),
(15, 2, 30, 'Caterpie', 'Grass', 'Basic', 'Early-stage common; evolves quickly', '10', 'Fire', NULL, 1, '10/64');


UPDATE tbl_collections
SET total_cards_collection = (
  SELECT COUNT(*) FROM tbl_cards WHERE tbl_cards.collection_id = tbl_collections.id
)
WHERE id IN (1,2,3,4,5);
