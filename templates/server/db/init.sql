DROP TABLE IF EXISTS `testTable1`;

CREATE TABLE `testTable1` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(20) NOT NULL,
  `tValue` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

#INSERT INTO testTable1 VALUE (1,'Clients','4 589');
INSERT INTO testTable1 (title,tValue) VALUES ('Clients','4 589'),('Transactions','789'),('Income','$1 999,99'),('Account','$19 999,99');