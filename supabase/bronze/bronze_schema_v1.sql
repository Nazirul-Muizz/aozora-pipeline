CREATE TABLE IF NOT EXISTS bronze.metadata (
    work_id BIGINT NOT NULL PRIMARY KEY,
    work_name TEXT NOT NULL,
    classification_number INT,
    publication_date DATE,
    last_updated DATE,
    book_url TEXT,
    person_id BIGINT,
    first_name_japanese TEXT,
    last_name_japanese TEXT,
    first_name_romaji TEXT,
    last_name_romaji TEXT,
    role TEXT,
    birth_date DATE,
    death_date DATE,
    ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);