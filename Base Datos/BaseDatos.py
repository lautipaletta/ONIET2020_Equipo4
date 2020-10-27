import sqlite3

connection = sqlite3.connect('example.db')
cursor = connection.cursor()


cmd = """CREATE TABLE IF NOT EXISTS APPCOVID(
            first TEXT NOT NULL,
            last TEXT NOT NULL,
            email TEXT NOT NULL PRIMARY KEY,
            password BLOB NOT NULL,
            country TEXT NOT NULL,
            slug TEXT NOT NULL,
            residence TEXT NOT NULL,
            lastlogin DATE
    )"""
cursor.execute(cmd)




#.pack_forget() PARA ESCONDER VENTANA



def ChangePassword(nextPassword, thisUser):
    if not nextPassword:
        cmd = f""" UPDATE APPCOVID SET password = {nextPassword} WHERE email == {thisUser} """ 
        cursor.execute(cmd)
        connection.commit()

def ChangeFirst(nextFirst, thisUser):
    if not nextFirst:
        cmd = f""" UPDATE APPCOVID SET first = {nextFirst} WHERE email == {thisUser} """
        cursor.execute(cmd)
        connection.commit()
    
def ChangeLast(nextLast, thisUser):
    if not nextLast:
        cmd = f""" UPDATE APPCOVID SET last = {nextLast} WHERE email == {thisUser} """
        cursor.execute(cmd)
        connection.commit()

def ChangeCountry(nextCountry, thisUser):
    if not nextCountry:
        cmd = f""" UPDATE APPCOVID SET country = {nextCountry} WHERE email == {thisUser} """
        cursor.execute(cmd)
        connection.commit()    

def ChangeSlug(nextSlug, thisUser):
    if not nextSlug:
        cmd = f""" UPDATE APPCOVID SET slug = {nextSlug} WHERE email == {thisUser} """
        cursor.execute(cmd)
        connection.commit()   

def ChangeResidence(nextResidence, thisUser):
    if not nextResidence:
        cmd = f""" UPDATE APPCOVID SET residence = {nextResidence} WHERE email == {thisUser} """
        cursor.execute(cmd)
        connection.commit()   





def ValidateLogin(Email, Password):
    cmd = f""" SELECT (password) FROM APPCOVID WHERE email = {Email} """
    cursor.execute(cmd)
    findedPassword = cursor.fetchone()

    if Password == findedPassword:
        
    else
        print("La contraseña no corresponde o no está permitida.")


