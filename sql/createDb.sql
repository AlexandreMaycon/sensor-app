CREATE SCHEMA `challenge` DEFAULT CHARACTER SET utf8;
use challenge;

CREATE TABLE equipment (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    equipmentId TEXT NOT NULL,
    timestamp TEXT NOT NULL,
    value REAL NOT NULL
);