-----> DATABASE: SERVICES <-----
/* DESCRIPTION: Database that contains the information about some services like music, videos, search engines etc. Basically the information about the methods to operate the services. */




--====================================================================================================================================================================================================
---> TABLE: Music services
/* DESCRIPTION: Table containing the information about the music services and their opeating metods. */
DROP TABLE IF EXISTS MUSIC_SERVICES;
CREATE TABLE MUSIC_SERVICES(name TEXT, host TEXT, searchMethod TEXT, playMethod TEXT, rank INT PRIMARY KEY, scrapMethod TEXT, status TEXT);
-----------------------------------------------------------------------------------------------------------------------------------------------------
INSERT INTO MUSIC_SERVICES VALUES("Ganna", "https://ganna.com", "/search/", "/song/", 1, "bs4", "RUN");
INSERT INTO MUSIC_SERVICES VALUES("Spotify", "https://spotify.com", " ", " ", 2, " ", "BUG");

----------------------




--====================================================================================================================================================================================================
---> TABLE: Video services
/* DESCRIPTION: Table containing the information about the video services and their opeating metods.*/
DROP TABLE IF EXISTS VIDEO_SERVICES;
CREATE TABLE VIDEO_SERVICES(name TEXT, host TEXT, searchMethod TEXT, playMethod TEXT, rank INT PRIMARY KEY, scrapMethod TEXT, status TEXT);
-----------------------------------------------------------------------------------------------------------------------------------------------------
INSERT INTO VIDEO_SERVICES VALUES("YouTube", "https://youtube.com", "/results?search_query=", "/watch?v=", 1, "bs4", "RUN");
INSERT INTO VIDEO_SERVICES VALUES("Dailymotion", "https://dailymotion.com", "/search/", "/video/", 2, " ", "BUG");

----------------------




--====================================================================================================================================================================================================
---> TABLE: Engines
/* DESCRIPTION: Table containing the information about the search engines and their search methods. */
DROP TABLE IF EXISTS ENGINES;
CREATE TABLE ENGINES(name TEXT PRIMARY KEY, method TEXT);
-----------------------------------------------------------------------------------------------------------------------------------------------------
INSERT INTO ENGINES VALUES('Google', '/search?q=');
INSERT INTO ENGINES VALUES('Bing', '/search?q=');
INSERT INTO ENGINES VALUES('Ask', '/web?q=');
INSERT INTO ENGINES VALUES('Yahoo', '/search?p=');
INSERT INTO ENGINES VALUES('Baidu', '/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=');
INSERT INTO ENGINES VALUES('Yendex', '/search/?lr=108944&text=');
INSERT INTO ENGINES VALUES('Duckduckgo', '/?q=');
INSERT INTO ENGINES VALUES('Swisscows', '/web?query=');
INSERT INTO ENGINES VALUES('Creative common', '/search?q=');
-- INSERT INTO ENGINES VALUES('', '');

----------------------




--====================================================================================================================================================================================================
---> TABLE: 
/* DESCRIPTION: */

