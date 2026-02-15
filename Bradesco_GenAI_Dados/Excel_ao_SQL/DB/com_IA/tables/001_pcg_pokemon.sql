
IF OBJECT_ID('dbo.tbl_cards', 'U') IS NOT NULL DROP TABLE dbo.tbl_cards;
IF OBJECT_ID('dbo.tbl_collections', 'U') IS NOT NULL DROP TABLE dbo.tbl_collections;

CREATE TABLE dbo.tbl_collections (
  id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
  collection_set_name VARCHAR(150) NOT NULL UNIQUE,
  release_date DATE NULL,
  total_cards_collection SMALLINT DEFAULT 0
);

CREATE TABLE dbo.tbl_cards (
  id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
  collection_id INT NULL,
  hp SMALLINT NULL,
  name VARCHAR(100) NOT NULL,
  type VARCHAR(50) NULL,
  stage VARCHAR(30) NULL,
  info VARCHAR(MAX) NULL,
  damage VARCHAR(20) NULL,
  weak VARCHAR(50) NULL,
  resist VARCHAR(50) NULL,
  retreat TINYINT NULL,
  card_number_in_collection VARCHAR(20) NULL,
  CONSTRAINT FK_cards_collection
    FOREIGN KEY (collection_id)
    REFERENCES dbo.tbl_collections (id)
    ON DELETE SET NULL
    ON UPDATE CASCADE
);

CREATE INDEX idx_collection_id ON dbo.tbl_cards(collection_id);
