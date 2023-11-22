import sqlite3

def create_database():
    connection = sqlite3.connect("PyFloraPosude.db")
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Korisnici (
            id INTEGER PRIMARY KEY,
            ime TEXT,
            prezime TEXT,
            korisničko_ime TEXT,
            password TEXT,
            status TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Biljke (
            id INTEGER PRIMARY KEY,
            naziv TEXT,
            slika BLOB,
            ideal_vlaznost TEXT,
            ideal_max_temp TEXT,
            ideal_min_temp TEXT,
            ideal_svjetlost TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Posude (
            id INTEGER PRIMARY KEY,
            lokacija TEXT,
            puna_prazna TEXT,
            naziv TEXT,
            vlaznost INTEGER,
            temperatura INTEGER,
            svjetlost INTEGER,
            FOREIGN KEY (naziv) REFERENCES Biljke (naziv)
        )
    ''')
    cursor.execute("INSERT INTO Korisnici (ime, prezime, korisničko_ime, password, status) VALUES ('Sanja', 'Oršolić', 'sorsolic', 'sanja1234', 'administrator')")
    connection.commit()
    connection.close()

create_database()
