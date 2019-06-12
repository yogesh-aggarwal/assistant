-----> DATABASE: PROGRAMINSTALLDATA <-----
/* DESCRIPTION: Database that contains the information about the programs that how they operate to make the assistant versatile and easily integratable with the programs that are installed on the PC. */




--=====================================================================================================================================================================================================
---> TABLE: Programs_data <---
/* DESCRIPTION: Table containing the information about the programs location and open method. */
DROP TABLE PROGRAMS_DATA;
CREATE TABLE PROGRAMS_DATA (name TEXT PRIMARY KEY, shortName1 TEXT DEFAULT '===', shortName2 TEXT DEFAULT '===', shortName3 TEXT DEFAULT '===', shortName4 TEXT DEFAULT '===', shortName5 TEXT DEFAULT '===', location TEXT, fileName TEXT, locationMethod Text, category TEXT);
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-- DEV APPS --
INSERT INTO PROGRAMS_DATA VALUES("Visual studio code", "Vs code", "Code studio", "===", "===", "===", "\AppData\Local\Programs\Microsoft VS Code", "code.exe", "user", "dev");
INSERT INTO PROGRAMS_DATA VALUES("Google chrome", "Chrome", "Chrome browser", "Browser", " ", " ", "C:\Program Files (x86)\Google\Chrome\Application", "chrome.exe", "self", "dev");


-- OFFICE APPLICATIONS --
INSERT INTO PROGRAMS_DATA VALUES("Microsoft word", "Word", "Office word", "Word office", "Ms word", "===", "C:\Program Files\Microsoft Office\root\Office16", "WINWORD.exe", "self", "work");
INSERT INTO PROGRAMS_DATA VALUES("Microsoft excel", "Excel", "Office excel", "Excel office", "Ms excel", "===", "C:\Program Files\Microsoft Office\root\Office16", "EXCEL.EXE", "self", "work");
INSERT INTO PROGRAMS_DATA VALUES("Microsoft powerpoint", "Powerpoint", "Office powerpoint", "Powerpoint office", "Ms powerpoint", "===", "C:\Program Files\Microsoft Office\root\Office16", "POWERPNT.EXE", "self", "work");
INSERT INTO PROGRAMS_DATA VALUES("Microsoft onenote", "Onenote", "Office onenote", "Onenote office", "Ms onenote", "Write book", "C:\Program Files\Microsoft Office\root\Office16", "ONENOTE.EXE", "self", "work");
INSERT INTO PROGRAMS_DATA VALUES("Microsoft outlook", "Outlook", "Office outlook", "Outlook office", "Ms outlook", "Ms mail", "C:\Program Files\Microsoft Office\root\Office16", "OUTLOOK.EXE", "self", "work");
-- INSERT INTO PROGRAMS_DATA VALUES("Microsoft onedrive", "Onedrive", " ", " ", "self", " ");
INSERT INTO PROGRAMS_DATA VALUES("Microsoft visio", "Visio", " ", " ", " ", " ", "C:\Program Files\Microsoft Office\root\Office16", "VISIO.EXE", "self", "work");
INSERT INTO PROGRAMS_DATA VALUES("Microsoft publisher", "Publisher", " ", " ", " ", " ", "C:\Program Files\Microsoft Office\root\Office16", "MSPUB.EXE", "self", "work");
INSERT INTO PROGRAMS_DATA VALUES("Microsoft access", "Access", " ", " ", " ", " ", "C:\Program Files\Microsoft Office\root\Office16", "MSACCESS.EXE", "self", "work");
INSERT INTO PROGRAMS_DATA VALUES("Microsoft project", "Project", " ", " ", " ", " ", "C:\Program Files\Microsoft Office\root\Office16", "WINPROJ.EXE", "self", "work");
INSERT INTO PROGRAMS_DATA VALUES("Microsoft skype", "Skype", " ", " ", " ", " ", "C:\Program Files\Microsoft Office\root\Office16", "lync.exe", "self", "work");


-- SYSTEM APPS --
INSERT INTO PROGRAMS_DATA VALUES("Control panel", "Control panel", " ", " ", " ", " ", "C:\WINDOWS\System32", "control.exe", "self", "sys");
INSERT INTO PROGRAMS_DATA VALUES("Command prompt", "Command line", "CMD", "Command stream", " ", " ", "C:\WINDOWS\System32", "conhost.exe", "self", "sys");
INSERT INTO PROGRAMS_DATA VALUES("Explorer", "Windows explorer", "File manager", "Microsoft explorer", "Ms explorer", "Manager", "C:\Windows", "explorer.exe", "self", "sys");
INSERT INTO PROGRAMS_DATA VALUES("Registry", "Windows registry", "Windows database", "===", "===", "===", "C:\Windows", "regedit.exe", "self", "sys");

-- INSERT INTO PROGRAMS_DATA VALUES("", " ", " ", " ", " ", " ", "", "", "", "");

----------------------




--====================================================================================================================================================================================================
---> TABLE: 
/* DESCRIPTION: */
