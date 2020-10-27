import sqlite3

def crearTabla():
    connection = sqlite3.connect("database")
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
    connection.commit()

#.pack_forget() PARA ESCONDER VENTANA

def Update(nextPassword, nextFirst, nextLast, nextCountry, nextSlug, nextResidence, thisUser):
    connection = sqlite3.connect("database")
    cursor = connection.cursor()
    cmd = f""" UPDATE APPCOVID
    SET password = {nextPassword},
        first = {nextFirst},
        last = {nextLast},
        country = {nextCountry},
        slug = {nextSlug},
        residence = {nextResidence}
    WHERE email == {thisUser}
        """ 
    cursor.execute(cmd)
    connection.commit()

def ValidateLogin(Email, Password):
    connection = sqlite3.connect("database")
    cursor = connection.cursor()
    cmd = f"SELECT (password) FROM APPCOVID WHERE email = '{Email}'"
    cursor.execute(cmd)
    findedPassword = cursor.fetchone()
    if Password == findedPassword[0]:
        return True
    else:
        return False

def SelectFrom(Email):
    connection = sqlite3.connect("database")
    cursor = connection.cursor()
    cmd = f"SELECT * FROM APPCOVID WHERE email = '{Email}'"
    cursor.execute(cmd)
    resultado = cursor.fetchone()
    return resultado

def agregar():
    connection = sqlite3.connect("database")
    cursor = connection.cursor()
    cmd = f"INSERT INTO APPCOVID VALUES ('Lautaro','Paletta','lautaro@hotmail.com','admin','Argentina','argentina','Quilmes','2020/27/10')"
    cursor.execute(cmd)
    connection.commit()


