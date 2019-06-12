-----> DATABASE: ATTRIBUTES <-----
/* DESCRIPTION: Database that contains the attributes about the assistant like user stored info, cache, information about the wen required to operate the assistant. */




--=====================================================================================================================================================================================================
---> TABLE: Keywords <---
/* DESCRIPTION: Table containing the information about the keywords used by the assistant for interacting properly with the user. */
DROP TABLE IF EXISTS KEYWORDS;
CREATE TABLE KEYWORDS(TYPE TEXT PRIMARY KEY, KEYWORDS TEXT);
-----------------------------------------------------------------------------------------------------------------------------------------------------
INSERT INTO KEYWORDS VALUES("QUESTION", "(WHAT, WHO, WHERE, HOW, WHOSE, WHOM, WHICH, WHY, WHEN)");

----------------------




--=====================================================================================================================================================================================================
---> TABLE: Domain <---
/* DESCRIPTION: Table containing the information about the domains and their usage. */
DROP TABLE IF EXISTS DOMAIN;
CREATE TABLE DOMAIN(NAME TEXT UNIQUE, USAGE TEXT, CATEGORY TEXT);
-----------------------------------------------------------------------------------------------------------------------------------------------------
INSERT INTO DOMAIN VALUES('COMMERCIAL', '.com', 'TLD');
INSERT INTO DOMAIN VALUES('EDUCATION', '.edu', 'TLD');
INSERT INTO DOMAIN VALUES('NETWORK', '.net', 'TLD');

----------------------




--====================================================================================================================================================================================================
---> TABLE: User_data
/* DESCRIPTION: Table that contains information about the user and its preferences. */
DROP TABLE IF EXISTS USER_DATA;
CREATE TABLE DOMAIN(NAME TEXT UNIQUE, USAGE TEXT, CATEGORY TEXT);
-----------------------------------------------------------------------------------------------------------------------------------------------------
INSERT INTO DOMAIN VALUES('COMMERCIAL', '.com', 'TLD');

----------------------




--====================================================================================================================================================================================================
---> TABLE: 
/* DESCRIPTION: */
