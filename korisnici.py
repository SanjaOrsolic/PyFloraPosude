import sqlite3
from tkinter import *
from tkinter import ttk

def korisnici_update():
    def prikazi_poruku(naslov, poruka):
        dialog = Toplevel(root5)
        dialog.geometry("400x100+100+100")
        dialog.config(bg="#f5f6f2")
        dialog.title(naslov)
        poruka=Label(dialog, text=poruka, bg="#f5f6f2", font=("Comic Sans MS", 12))
        poruka.place(x=10,y=30)
    root5 = Toplevel()
    root5.title("PyFloraPosude")
    root5.geometry("700x600+100+100")
    root5.config(bg="#f5f6f2")
    root5.resizable(False, False)

    slika_pozadine = PhotoImage(file="slike_za_gui\pozadina.png")
    pozadina = Label(root5, image=slika_pozadine)
    pozadina.place(x=0, y=0)

    frame_naslov = Frame(root5, bg="#f3edea", width=700, height=50)
    frame_naslov.place(x=0, y=0)
    naslov = Label(frame_naslov, text="PyFloraPosude", font=("Comic Sans MS", 16), bg="#f3edea")
    naslov.place(x=20, y=15)
    naslov_korisnici = Label(root5, text="Upravljanje korisnicima", font=("Comic Sans MS", 16), bg="#f3edea")
    naslov_korisnici.place(x=250, y=30)

    txt_ime = Label(root5, text="Ime", font=("Comic Sans MS", 12), bg="#f3edea")
    txt_ime.place(x=100, y=60)
    reg_ime = Entry(root5, width=15, font=("Comic Sans MS", 12))
    reg_ime.place(x=100, y=90)
    txt_prezime = Label(root5, text="Prezime", font=("Comic Sans MS", 12), bg="#f3edea")
    txt_prezime.place(x=100, y=130)
    reg_prezime = Entry(root5, width=15, font=("Comic Sans MS", 12))
    reg_prezime.place(x=100, y=160)
    txt_username = Label(root5, text="User Name", font=("Comic Sans MS", 12), bg="#f3edea")
    txt_username.place(x=100, y=190)
    reg_username = Entry(root5, width=15, font=("Comic Sans MS", 12))
    reg_username.place(x=100, y=220)
    txt_password = Label(root5, text="Password", font=("Comic Sans MS", 12), bg="#f3edea")
    txt_password.place(x=100, y=250)
    reg_password = Entry(root5, width=15, font=("Comic Sans MS", 12))
    reg_password.place(x=100, y=280)
    txt_status = Label(root5, text="Status korisnika (admin/korisnik)", font=("Comic Sans MS", 12), bg="#f3edea")
    txt_status.place(x=100, y=320)
    reg_status = Entry(root5, width=15, font=("Comic Sans MS", 12))
    reg_status.place(x=100, y=350)

    def prikazi_korisnike():
        tree.delete(*tree.get_children())  

        conn = sqlite3.connect("PyFloraPosude.db")
        cursor = conn.cursor()
        cursor.execute("SELECT ime, prezime, korisničko_ime, password, status FROM Korisnici")
        korisnici = cursor.fetchall()
        conn.close()

        for korisnik in korisnici:
            tree.insert("", "end", values=korisnik)

    def azuriraj_korisnika():
        selected_item = tree.selection()[0]
        values = tree.item(selected_item, "values")

        novo_ime = reg_ime.get()
        novo_prezime = reg_prezime.get()
        novo_username = reg_username.get()
        nova_lozinka = reg_password.get()
        novo_status = reg_status.get()

        conn = sqlite3.connect("PyFloraPosude.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE Korisnici SET ime=?, prezime=?, korisničko_ime=?, password=?, status=? WHERE korisničko_ime=?",
                    (novo_ime, novo_prezime, novo_username, nova_lozinka, novo_status, values[2]))
        conn.commit()
        conn.close()

        
        tree.item(selected_item, values=(novo_ime, novo_prezime, novo_username, nova_lozinka, novo_status))
        prikazi_poruku("Ažuriranje korisnika", "Korisnik je uspješno ažuriran!")
    def odaberi_korisnika(event):
        selected_item = tree.selection()[0]
        values = tree.item(selected_item, "values")

        reg_ime.delete(0, END)
        reg_ime.insert(0, values[0])

        reg_prezime.delete(0, END)
        reg_prezime.insert(0, values[1])

        reg_username.delete(0, END)
        reg_username.insert(0, values[2])

        reg_password.delete(0, END)
        reg_password.insert(0,values[3])

        reg_status.delete(0, END)
        reg_status.insert(0, values[4])

    def obrisi_korisnika():
        selected_item = tree.selection()[0]
        values = tree.item(selected_item, "values")

        conn = sqlite3.connect("PyFloraPosude.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Korisnici WHERE korisničko_ime=?", (values[2],))
        conn.commit()
        conn.close()

        tree.delete(selected_item)  
        prikazi_poruku("Brisanje korisnika", "Korisnik je uspješno obrisan!")
    
    tree = ttk.Treeview(root5, columns=("ime", "prezime", "username", "password","status"), show="headings")
    tree.heading("ime", text="Ime")
    tree.heading("prezime", text="Prezime")
    tree.heading("username", text="Korisničko ime")
    tree.heading("password", text="Password")
    tree.heading("status", text="Status")

    tree.column("ime", width=120)  
    tree.column("prezime", width=120)  
    tree.column("username", width=120)  
    tree.column("password", width=120)  
    tree.column("status", width=120)
    tree["height"] = 6
    tree.place(x=60, y=400)

    gumb_1 = Button(root5, text="Pregledaj korisnike", bg="#a7c47a", font=("Comic Sans MS", 12), width=15,
                    command=prikazi_korisnike)
    gumb_1.place(x=440, y=150)

    gumb_2 = Button(root5, text="Ažuriraj korisnika", bg="#a7c47a", font=("Comic Sans MS", 12), width=15,
                command=azuriraj_korisnika)
    gumb_2.place(x=440, y=200)

    
    tree.bind("<ButtonRelease-1>", odaberi_korisnika)

    gumb_3 = Button(root5, text="Obriši korisnika", bg="#a7c47a", font=("Comic Sans MS", 12), width=15,
                    command=obrisi_korisnika)
    gumb_3.place(x=440, y=250)


    root5.mainloop()

