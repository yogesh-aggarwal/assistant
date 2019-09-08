USE ASSISTANT;

/*
DROP TABLE IF EXISTS PROGRAMS_DATA;
CREATE TABLE PROGRAMS_DATA
(
    name VARCHAR(30) PRIMARY KEY,
    shortName1 TEXT,
    shortName2 TEXT,
    shortName3 TEXT,
    shortName4 TEXT,
    shortName5 TEXT,
    location TEXT,
    fileName TEXT,
    locationMethod Text,
    category TEXT,
    openMethod TEXT
);

INSERT INTO PROGRAMS_DATA
VALUES("Visual studio code", "Vs code", "Code studio", "===", "===", "===", "\AppData\Local\Programs\Microsoft VS Code", "code.exe", "user", "dev", "exe");
INSERT INTO PROGRAMS_DATA
VALUES("Google chrome", "Chrome", "Chrome browser", "Browser", "===", "===", "C:\Program Files (x86)\Google\Chrome\Application", "chrome.exe", "self", "dev", "exe");

INSERT INTO PROGRAMS_DATA
VALUES("Microsoft word", "Word", "Office word", "Word office", "Ms word", "===", "C:\Program Files\Microsoft Office\root\Office16", "WINWORD.exe", "self", "work", "exe");
INSERT INTO PROGRAMS_DATA
VALUES("Microsoft excel", "Excel", "Office excel", "Excel office", "Ms excel", "===", "C:\Program Files\Microsoft Office\root\Office16", "EXCEL.EXE", "self", "work", "exe");
INSERT INTO PROGRAMS_DATA
VALUES("Microsoft powerpoint", "Powerpoint", "Office powerpoint", "Powerpoint office", "Ms powerpoint", "===", "C:\Program Files\Microsoft Office\root\Office16", "POWERPNT.EXE", "self", "work", "exe");
INSERT INTO PROGRAMS_DATA
VALUES("Microsoft onenote", "Onenote", "Office onenote", "Onenote office", "Ms onenote", "Write book", "C:\Program Files\Microsoft Office\root\Office16", "ONENOTE.EXE", "self", "work", "exe");
INSERT INTO PROGRAMS_DATA
VALUES("Microsoft outlook", "Outlook", "Office outlook", "Outlook office", "Ms outlook", "Ms mail", "C:\Program Files\Microsoft Office\root\Office16", "OUTLOOK.EXE", "self", "work", "exe");

INSERT INTO PROGRAMS_DATA
VALUES("Microsoft visio", "Visio", "===", "===", "===", "===", "C:\Program Files\Microsoft Office\root\Office16", "VISIO.EXE", "self", "work", "exe");
INSERT INTO PROGRAMS_DATA
VALUES("Microsoft publisher", "Publisher", "===", "===", "===", "===", "C:\Program Files\Microsoft Office\root\Office16", "MSPUB.EXE", "self", "work", "exe");
INSERT INTO PROGRAMS_DATA
VALUES("Microsoft access", "Access", "===", "===", "===", "===", "C:\Program Files\Microsoft Office\root\Office16", "MSACCESS.EXE", "self", "work", "exe");
INSERT INTO PROGRAMS_DATA
VALUES("Microsoft project", "Project", "===", "===", "===", "===", "C:\Program Files\Microsoft Office\root\Office16", "WINPROJ.EXE", "self", "work", "exe");
INSERT INTO PROGRAMS_DATA
VALUES("Microsoft skype", "Skype", "===", "===", "===", "===", "C:\Program Files\Microsoft Office\root\Office16", "lync.exe", "self", "work", "exe");



INSERT INTO PROGRAMS_DATA
VALUES("Control panel", "Control panel", "===", "===", "===", "===", "C:\WINDOWS\System32", "control.exe", "self", "sys", "exe");
INSERT INTO PROGRAMS_DATA
VALUES("Command prompt", "Command line", "CMD", "Command stream", "===", "===", "C:\WINDOWS\System32", "conhost.exe", "self", "sys", "exe");
INSERT INTO PROGRAMS_DATA
VALUES("Explorer", "Windows explorer", "File manager", "Microsoft explorer", "Ms explorer", "File explorer", "C:\Windows", "explorer.exe", "self", "sys", "exe");
INSERT INTO PROGRAMS_DATA
VALUES("Registry", "Windows registry", "Windows database", "===", "===", "===", "C:\Windows", "regedit.exe", "self", "sys", "exe");
INSERT INTO PROGRAMS_DATA
VALUES("Notepad", "Windows notepad", "Microsoft notepad", "Ms notepad", "===", "===", "C:\Windows", "regedit.exe", "self", "sys", "exe");

INSERT INTO PROGRAMS_DATA
VALUES("Music", "Microsoft music", "Ms music", "Music player", "Groove", "Groove music", "===", "start mswindowsmusic:", "self", "sys", "command");

INSERT INTO PROGRAMS_DATA
VALUES("Calculator", "Microsoft calculator", "Ms calculator", "===", "===", "===", "===", "start ms-calculator:", "self", "sys", "command");
INSERT INTO PROGRAMS_DATA
VALUES("Camera", "Microsoft camera", "Ms camera", "===", "===", "===", "===", "start microsoft.windows.camera:", "self", "sys", "command");
INSERT INTO PROGRAMS_DATA
VALUES("Alarms", "Microsoft alarms", "Ms alarms", "Alarms and clock", "Ms alarms and clock", "Clock", "===", "start explorer.exe shell:AppsFolder\Microsoft.WindowsAlarms_8wekyb3d8bbwe!App", "self", "sys", "command");
INSERT INTO PROGRAMS_DATA
VALUES("Settings", "Microsoft settings", "Ms settings", "System settings", "===", "===", "===", "start ms-settings:", "self", "sys", "command");
INSERT INTO PROGRAMS_DATA
VALUES("Edge", "Edge browser", "Microsoft edge", "Ms edge", "Microsoft edge browser", "Ms edge browser", "===", "start microsoft-edge:", "self", "sys", "command");
INSERT INTO PROGRAMS_DATA
VALUES("Media player", "Windows media player", "Microsoft windows media player", "Ms windows media player", "Ms media player", "===", "===", "start wmplayer.exe", "self", "sys", "command");
*/

SELECT * FROM PROGRAMS_DATA
