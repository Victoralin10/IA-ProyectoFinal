
-- Dataset
CREATE TABLE IF NOT EXISTS `dataset` (
  `id`         VARCHAR(32)  NOT NULL,
  `anio`       MEDIUMINT(9) NOT NULL,
  `mes`        TINYINT(4)   NOT NULL,
  `dia`        TINYINT(4)   NOT NULL,
  `dia_semana` TINYINT(4)   NOT NULL,
  `hora`       TINYINT(4)   NOT NULL,
  `minuto`     TINYINT(4)   NOT NULL,
  `segundo`    TINYINT(4)   NOT NULL,
  `tag`        VARCHAR(100) NULL DEFAULT NULL,
  `tagger`     VARCHAR(50)  NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `dataset_index` (`tag` ASC)
);

-- Tags
CREATE TABLE IF NOT EXISTS `tags` (
  `code`        VARCHAR(10)  NOT NULL,
  `description` VARCHAR(128) NULL,
  PRIMARY KEY (`code`)
);

-- events
CREATE TABLE IF NOT EXISTS `events` (
  `id`        INT          NOT NULL AUTO_INCREMENT,
  `station`     VARCHAR(64)  NULL,
  `description`   VARCHAR(256) NULL,
  `timestamp` TIMESTAMP    NULL,
  PRIMARY KEY (`id`)
);

insert into `tags` (`code`, `description`)
values
  ('j01', 'Raúl Vargas'),
  ('j02', 'Mónica Delta'),
  ('j03', 'Helmer Huerta'),
  ('j04', 'Guillermo Rossinni'),
  ('j05', 'Hector Felipe'),
  ('j06', 'Patricia del Rio'),
  ('jxx', 'Otro');
