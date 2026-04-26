-- Удаляем старые таблицы, если они вдруг есть, чтобы начать с чистого листа
DROP TABLE IF EXISTS phones CASCADE;
DROP TABLE IF EXISTS contacts CASCADE;
DROP TABLE IF EXISTS groups CASCADE;

-- 1. Таблица групп (Family, Work, Friend, Other)
CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

-- 2. Основная таблица контактов (сразу с email и днем рождения)
CREATE TABLE contacts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(100),
    birthday DATE,
    group_id INTEGER REFERENCES groups(id) ON DELETE SET NULL
);

-- 3. Таблица телефонов (связь 1-ко-многим)
CREATE TABLE phones (
    id SERIAL PRIMARY KEY,
    contact_id INTEGER REFERENCES contacts(id) ON DELETE CASCADE,
    phone VARCHAR(20) NOT NULL,
    type VARCHAR(10) CHECK (type IN ('home', 'work', 'mobile'))
);

-- Добавим базовые группы для старта
INSERT INTO groups (name) VALUES ('Family'), ('Work'), ('Friend'), ('Other');