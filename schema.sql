BEGIN;
CREATE TABLE `trabajo` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(150) NOT NULL UNIQUE,
    `slug` varchar(50) NOT NULL UNIQUE,
    `description` longtext NOT NULL,
    `photoset_id` varchar(255) NOT NULL,
    `created` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
COMMIT;
