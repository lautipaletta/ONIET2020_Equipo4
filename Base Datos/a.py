import sqlite3

CREATE TABLE [IF NOT EXISTS] APPCOVID (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    first TEXT NOT NULL ,
	last TEXT NOT NULL,
	email TEXT NOT NULL,
    password BLOB NOT NULL,
    country TEXT NOT NULL,
    countrycode TEXT NOT NULL
)



def CambiarPassword(nextPassword, thisUser):
    cmd = f""" UPDATE APPCOVID SET password = {nextPassword} WHERE email LIKE {thisUser} """ 

def CambiarFirst(nextFirst, thisUser):
    cmd = f""" UPDATE APPCOVID SET password = {nextFirst} WHERE email LIKE {thisUser} """

def CambiarLast(nextLast, thisUser):
    cmd = f""" UPDATE APPCOVID SET password = {nextLast} WHERE email LIKE {thisUser} """

def CambiarEmail(nextEmail, thisUser):
    cmd = f""" UPDATE APPCOVID SET password = {nextEmail} WHERE email LIKE {thisUser} """

def CambiarCountry(nextCountry, thisUser):
    cmd = f""" UPDATE APPCOVID SET password = {nextCountry} WHERE email LIKE {thisUser} """

def CambiarCountryCode(nextCountryCode, thisUser):
    cmd = f""" UPDATE APPCOVID SET password = {nextCountryCode} WHERE email LIKE {thisUser} """






