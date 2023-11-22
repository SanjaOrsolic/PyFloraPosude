from tkinter import*
from tkinter import messagebox
from Gl_prozor_app import prijava_u_gl_prozor
import sqlite3


def prijava():
    x_unos=unos_username.get()
    y_unos=unos_password.get()
    unos_username.delete(0,END)
    unos_password.delete(0,END)

    conn = sqlite3.connect("PyFloraPosude.db")
    cursor = conn.cursor()

    cursor.execute("SELECT ime, prezime, status FROM Korisnici WHERE korisničko_ime=? AND password=?", (x_unos, y_unos))
    korisnik_info = cursor.fetchone()
    
    conn.close()

    if korisnik_info:
        ime, prezime, status = korisnik_info
        prijava_u_gl_prozor(ime, prezime, status)
        
    else:
        messagebox.showinfo("Prijava", "Prijava je neuspješna!")

def registracija():
    def unos_novih_korisnika():
        ime=reg_ime.get()
        prezime=reg_prezime.get()
        username=reg_username.get()
        password=reg_password.get()
        status=reg_status.get()
        conn = sqlite3.connect("PyFloraPosude.db")
        cursor = conn.cursor()
        if ime!="" and prezime!="" and username!="" and password!="":
            cursor.execute("INSERT INTO Korisnici (ime, prezime, korisničko_ime, password, status) VALUES (?,?,?,?,?)", (ime, prezime, username, password, status))
            root2.destroy()
            
            messagebox.showinfo("Unos korisnika", "Korisnik je uspješno kreiran!")
            conn.commit()
            conn.close()
        else:
            messagebox.showinfo("Unos korisnika", "Nisu unesena sva polja za registraciju!")

    root2=Toplevel()
    root2.title("PyFloraPosude")
    root2.geometry("700x600+100+100")
    root2.config(bg="#f5f6f2")
    root2.resizable(False, False)
    slika_pozadine=PhotoImage(file="slike_za_gui\pozadina.png")
    pozadina=Label(root2, image=slika_pozadine)
    pozadina.place(x=0,y=0)
    frame_naslov1=Frame(root2, bg="#f3edea", width=700 ,height=50)
    frame_naslov1.place(x=0,y=0)
    naslov1=Label(frame_naslov1, text="PyFloraPosude", font=("Comic Sans MS",16),bg="#f3edea")
    naslov1.place(x=20,y=15)
    naslov2=Label(root2, text="Registracija", font=("Comic Sans MS",16),bg="#f3edea")
    naslov2.place(x=300,y=60)
    txt_ime=Label(root2, text="Ime", font=("Comic Sans MS",12,),bg="#f3edea")
    txt_ime.place(x=200,y=110)
    reg_ime=Entry(root2, width=15, font=("Comic Sans MS",12))
    reg_ime.place(x=200,y=140)
    txt_prezime=Label(root2, text="Prezime", font=("Comic Sans MS",12,),bg="#f3edea")
    txt_prezime.place(x=200,y=180)
    reg_prezime=Entry(root2, width=15, font=("Comic Sans MS",12))
    reg_prezime.place(x=200,y=210)
    txt_username=Label(root2, text="User Name", font=("Comic Sans MS",12,),bg="#f3edea")
    txt_username.place(x=200,y=240)
    reg_username=Entry(root2, width=15, font=("Comic Sans MS",12))
    reg_username.place(x=200,y=270)
    txt_password=Label(root2, text="Password", font=("Comic Sans MS",12),bg="#f3edea")
    txt_password.place(x=200,y=300)
    reg_password=Entry(root2, width=15, font=("Comic Sans MS",12))
    reg_password.place(x=200,y=330)
    tex_status=Label(root2, text="Status korisnika (admin/korisnik)", font=("Comic Sans MS",12),bg="#f3edea")
    tex_status.place(x=200,y=370)
    reg_status=Entry(root2, width=15, font=("Comic Sans MS",12))
    reg_status.place(x=200,y=400)
    gumb_2=Button(root2, text="Unesi", bg="#a7c47a", font=("Comic Sans MS",12),width=10,command=unos_novih_korisnika)
    gumb_2.place(x=240,y=430)

    root2.mainloop()

root=Tk()
root.title("PyFloraPosude")
root.focus
root.geometry("700x600+100+100")
root.config(bg="#f5f6f2")
root.resizable(False, False)

slika_pozadine=PhotoImage(file="slike_za_gui\pozadina.png")
pozadina=Label(root, image=slika_pozadine)
pozadina.place(x=0,y=0)

frame_naslov=Frame(root, bg="#f3edea", width=700 ,height=50)
frame_naslov.place(x=0,y=0)
naslov=Label(frame_naslov, text="PyFloraPosude", font=("Comic Sans MS",16),bg="#f3edea")
naslov.place(x=20,y=15)
naslov_2=Label(root, text="Prijava", font=("Comic Sans MS",16),bg="#f3edea")
naslov_2.place(x=350,y=80)

tekst_username=Label(root, text="User Name", font=("Comic Sans MS",12,),bg="#f3edea")
tekst_username.place(x=340,y=130)
unos_username=Entry(root, width=15, font=("Comic Sans MS",12))
unos_username.place(x=290,y=160)
tekst_password=Label(root, text="Password", font=("Comic Sans MS",12),bg="#f3edea")
tekst_password.place(x=340,y=210)
unos_password=Entry(root, width=15, font=("Comic Sans MS",12),show="*")
unos_password.place(x=290,y=240)


gumb_1=Button(root, text="Prijava", bg="#a7c47a", font=("Comic Sans MS",12),width=10,command=prijava )
gumb_1.place(x=260,y=300)
gumb_2=Button(root, text="Registracija", bg="#a7c47a", font=("Comic Sans MS",12),width=10,command=registracija)
gumb_2.place(x=390,y=300)

root.mainloop()