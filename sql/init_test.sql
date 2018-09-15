-- 测试环境
CREATE SCHEMA `xigua_test` ;

DROP TABLE IF EXISTS `jce_change_subscriber`;

CREATE TABLE `jce_change_subscriber` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `qxwx_login_id` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;