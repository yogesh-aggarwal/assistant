-----> DATABASE: ATTRIBUTES <-----
/* DESCRIPTION: Database that contains the attributes about the assistant like user stored info, cache, information about the wen required to operate the assistant. */




--=====================================================================================================================================================================================================
---> TABLE: KEYWORDS <---
/* DESCRIPTION: Table containing the information about the keywords used by the assistant for interacting properly with the user. */
DROP TABLE IF EXISTS KEYWORDS;
CREATE TABLE KEYWORDS(type TEXT PRIMARY KEY, keywords TEXT);
-----------------------------------------------------------------------------------------------------------------------------------------------------
INSERT INTO KEYWORDS VALUES("QUESTION", "(WHAT, WHO, WHERE, HOW, WHOSE, WHOM, WHICH, WHY, WHEN)");

----------------------




--====================================================================================================================================================================================================
---> TABLE: USER_ATTRIBUTES
/* DESCRIPTION: Table that contains the information about the user preferences and the data.AUTOINCREMENT */
DROP TABLE IF EXISTS USER_ATTRIBUTES;
CREATE TABLE USER_ATTRIBUTES(name TEXT, value TEXT);
-----------------------------------------------------------------------------------------------------------------------------------------------------

INSERT INTO USER_ATTRIBUTES VALUES("videoDirectory", "D:\Videos\Music Videos");
INSERT INTO USER_ATTRIBUTES VALUES("musicDirectory", "D:\Music\All time Music");

----------------------
