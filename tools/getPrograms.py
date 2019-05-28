import win32com.client

from sql_operation import Sqlite3 as sql

sql().execute("CREATE TABLE IF NOT EXISTS PROGRAMS(CAPTION TEXT, DESCRIPTION TEXT, IDENTIFYING NUMBER TEXT, INSTALL_DATE TEXT, INSTALL_DATE_2 TEXT, INSTALL_LOCATION TEXT, INSTALL_STATE TEXT, NAME TEXT, PACKAGE CACHE TEXT, SKU NUMBER TEXT, VENDOR TEXT, VERSION TEXT);")

strComputer = "." 
objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator") 
objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2") 
colItems = objSWbemServices.ExecQuery("Select * from Win32_Product") 

for objItem in colItems:
    sql().execute(f"INSERT INTO PROGRAMS VALUES('{objItem.Caption}', '{objItem.Description}', '{objItem.IdentifyingNumber}', '{objItem.InstallDate}', '{objItem.InstallDate2}', '{objItem.InstallLocation}', '{objItem.InstallState}', '{objItem.Name}', '{objItem.PackageCache}', '{objItem.SKUNumber}', '{objItem.Vendor}', '{objItem.Version}');")
