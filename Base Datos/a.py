import sqlite3

connection = sqlite3.connect('example.db')
cursor = connection.cursor()


cmd = """CREATE TABLE IF NOT EXISTS APPCOVID(
            first TEXT NOT NULL ,
            last TEXT NOT NULL,
            email TEXT NOT NULL PRIMARY KEY,
            password BLOB NOT NULL,
            country TEXT NOT NULL,
            countrycode TEXT NOT NULL,
            lastlogin DATE
    )"""
cursor.execute(cmd)


def CambiarPassword(nextPassword, thisUser):
    cmd = f""" UPDATE APPCOVID SET password = {nextPassword} WHERE email LIKE {thisUser} """ 
    cursor.execute(cmd)
    connection.commit()

def CambiarFirst(nextFirst, thisUser):
    cmd = f""" UPDATE APPCOVID SET password = {nextFirst} WHERE email LIKE {thisUser} """
    cursor.execute(cmd)
    connection.commit()
    
def CambiarLast(nextLast, thisUser):
    cmd = f""" UPDATE APPCOVID SET password = {nextLast} WHERE email LIKE {thisUser} """
    cursor.execute(cmd)
    connection.commit()

def CambiarEmail(nextEmail, thisUser):
    cmd = f""" UPDATE APPCOVID SET password = {nextEmail} WHERE email LIKE {thisUser} """
    cursor.execute(cmd)
    connection.commit()

def CambiarCountry(nextCountry, thisUser):
    cmd = f""" UPDATE APPCOVID SET password = {nextCountry} WHERE email LIKE {thisUser} """
    cursor.execute(cmd)
    connection.commit()    

def CambiarCountryCode(nextCountryCode, thisUser):
    cmd = f""" UPDATE APPCOVID SET password = {nextCountryCode} WHERE email LIKE {thisUser} """
    cursor.execute(cmd)
    connection.commit()    

