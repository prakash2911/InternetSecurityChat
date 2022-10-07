
CREATE TABLE `chitchat`.`account` (
  `username` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NULL,
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE,
  PRIMARY KEY (`username`));

INSERT INTO `chitchat`.`account` (`username`, `password`) VALUES ('prakash', '1234');
INSERT INTO `chitchat`.`account` (`username`, `password`) VALUES ('guru', '1234');

CREATE TABLE `chitchat`.`chat_maintance` (
  `from` VARCHAR(45) NOT NULL,
  `to` VARCHAR(45) NULL,
  `time` TIME NOT NULL,
  `date` DATE NOT NULL,
  `msg` LONGTEXT NULL,
  `chat_maintancecol` VARCHAR(45) NULL,
  PRIMARY KEY (`time`, `date`));

CREATE TABLE `chitchat`.`key_maintance` (
  `user` VARCHAR(45) NOT NULL,
  `key` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`user`),
  UNIQUE INDEX `key_UNIQUE` (`key` ASC) VISIBLE);
