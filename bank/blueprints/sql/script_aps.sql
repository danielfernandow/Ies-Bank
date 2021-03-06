/*
CREATE DATABASE "APS-2021-1"
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Portuguese_Brazil.1252'
    LC_CTYPE = 'Portuguese_Brazil.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;
*/

/*----------------------- TABLES -----------------------*/
CREATE TABLE PERSON (
  person_id SERIAL NOT NULL,
  adress_id INT NOT NULL,
  account_id INT NOT NULL,
  name VARCHAR(256) NOT NULL,
  password VARCHAR(512) NOT NULL,
  cpf VARCHAR(14) NOT NULL,
  birthdate DATE NOT NULL,
  email VARCHAR(128) NOT NULL
);

CREATE TABLE ACCOUNT (
  account_id SERIAL NOT NULL,
  account_status_id INT NOT NULL,
  agency INT NOT NULL,
  balance DECIMAL(16, 2) NOT NULL
);

CREATE TABLE ACCOUNT_STATUS (
  account_status_id SERIAL NOT NULL,
  description VARCHAR(64) NOT NULL
);

CREATE TABLE "TRANSACTION" (
  transaction_id SERIAL NOT NULL,
  account_id INT NOT NULL,
  transaction_type_id INT NOT NULL,
  transaction_status_id INT NOT NULL,
  transactionDate DATE NOT NULL,
  amount DECIMAL(16, 2) NOT NULL
);

CREATE TABLE TRANSACTION_STATUS (
  transaction_status_id SERIAL NOT NULL,
  description VARCHAR(64) NOT NULL
);

CREATE TABLE TRANSACTION_TYPE (
  transaction_type_id SERIAL NOT NULL,
  description VARCHAR(64) NOT NULL
);

CREATE TABLE ADRESS (
  adress_id SERIAL NOT NULL,
  telephone_id INT NOT NULL,
  state_id INT NOT NULL,
  city VARCHAR(64) NOT NULL,
  adress VARCHAR(256) NOT NULL,
  number VARCHAR(32) NOT NULL,
  district VARCHAR(64) NOT NULL,
  zipCode VARCHAR(9)
);

CREATE TABLE TELEPHONE (
  telephone_id SERIAL NOT NULL,
  ddd VARCHAR(3) NOT NULL,
  number VARCHAR(10) NOT NULL
);

CREATE TABLE STATE ( 
  state_id SERIAL NOT NULL,
  name VARCHAR(32) NOT NULL,
  initials VARCHAR(2) NOT NULL
);

/*----------------------- PRIMARY KEYS -----------------------*/
ALTER TABLE PERSON ADD PRIMARY KEY (person_id);
ALTER TABLE ACCOUNT ADD PRIMARY KEY (account_id);
ALTER TABLE ACCOUNT_STATUS ADD PRIMARY KEY (account_status_id);
ALTER TABLE "TRANSACTION" ADD PRIMARY KEY (transaction_id);
ALTER TABLE TRANSACTION_STATUS ADD PRIMARY KEY (transaction_status_id);
ALTER TABLE TRANSACTION_TYPE ADD PRIMARY KEY (transaction_type_id);
ALTER TABLE ADRESS ADD PRIMARY KEY (adress_id);
ALTER TABLE TELEPHONE ADD PRIMARY KEY (telephone_id);
ALTER TABLE STATE ADD PRIMARY KEY (state_id);

/*----------------------- FOREIGN KEYS -----------------------*/
ALTER TABLE PERSON ADD CONSTRAINT FK_PERSON_ADRESS
FOREIGN KEY (adress_id) REFERENCES ADRESS (adress_id)
ON UPDATE NO ACTION
ON DELETE NO ACTION;

ALTER TABLE PERSON ADD CONSTRAINT FK_PERSON_ACCOUNT
FOREIGN KEY (account_id) REFERENCES ACCOUNT (account_id)
ON UPDATE NO ACTION
ON DELETE NO ACTION;

ALTER TABLE ACCOUNT ADD CONSTRAINT FK_ACCOUNT_ACCOUNT_STATUS
FOREIGN KEY (account_status_id) REFERENCES ACCOUNT_STATUS (account_status_id)
ON UPDATE NO ACTION
ON DELETE NO ACTION;

ALTER TABLE "TRANSACTION" ADD CONSTRAINT FK_TRANSACTION_ACCOUNT
FOREIGN KEY (account_id) REFERENCES ACCOUNT (account_id)
ON UPDATE NO ACTION
ON DELETE NO ACTION;

ALTER TABLE "TRANSACTION" ADD CONSTRAINT FK_TRANSACTION_TRANSACTION_TYPE
FOREIGN KEY (transaction_type_id) REFERENCES TRANSACTION_TYPE (transaction_type_id)
ON UPDATE NO ACTION
ON DELETE NO ACTION;

ALTER TABLE "TRANSACTION" ADD CONSTRAINT FK_TRANSACTION_TRANSACTION_STATUS
FOREIGN KEY (transaction_status_id) REFERENCES TRANSACTION_STATUS (transaction_status_id)
ON UPDATE NO ACTION
ON DELETE NO ACTION;

ALTER TABLE ADRESS ADD CONSTRAINT FK_ADRESS_TELEPHONE
FOREIGN KEY (telephone_id) REFERENCES TELEPHONE (telephone_id)
ON UPDATE NO ACTION
ON DELETE NO ACTION;

ALTER TABLE ADRESS ADD CONSTRAINT FK_ADRESS_STATE
FOREIGN KEY (state_id) REFERENCES STATE (state_id)
ON UPDATE NO ACTION
ON DELETE NO ACTION;



INSERT INTO account_status (description) VALUES (
	'asdas'
)

INSERT INTO account (account_status_id, agency, balance) VALUES (
	1, 1, 23.5
)

INSERT INTO telephone (ddd, number) VALUES (
	'39', '959955'
)

INSERT INTO state (name, initials) VALUES (
	'oasdkosa', 'sc'
)

INSERT INTO adress (telephone_id, state_id, city, adress, number, district, zipCode) VALUES (
	1, 1, 'sdoakd', 'aosdkaso', 'oaskdoas', 'aosdksaodkk', 'aosdk'
)

INSERT INTO person (adress_id, account_id, name, password, cpf, birthdate, email) VALUES (
	3, 1, 'bank teste', 'aksoek', '0685269323', '20/06/1995', 'daniel@gmail.com'
)