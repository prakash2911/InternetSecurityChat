CREATE SCHEMA `chitchat` ;

CREATE TABLE `chitchat`.`account` (
  `username` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NULL,
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE,
  PRIMARY KEY (`username`));

INSERT INTO `chitchat`.`account` (`username`, `password`) VALUES ('prakash', '1234');
    