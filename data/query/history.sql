-----> DATABASE: PROGRAMINSTALLDATA <-----
/* DESCRIPTION: Database that contains the information about the queries provided to the assistant for better analysis. */




--=====================================================================================================================================================================================================
---> TABLE: HISTORY
/* DESCRIPTION: Table that contains the information about whether the query solved or not. */
DROP TABLE IF EXISTS HISTORY;
CREATE TABLE HISTORY(query TEXT, solved TEXT);
-----------------------------------------------------------------------------------------------------------------------------------------------------

----------------------
