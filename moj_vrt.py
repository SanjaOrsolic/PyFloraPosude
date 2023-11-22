import sqlite3
import random
from tkinter import *
from tkinter import ttk

def prijava_moj_vrt():
    def prikazi_poruku(naslov, poruka):
        dialog = Toplevel(root)
        dialog.geometry("320x100+300+300")
        dialog.config(bg="#f5f6f2")
        dialog.title(naslov)
        poruka=Label(dialog, text=poruka, bg="#f5f6f2", font=("Comic Sans MS", 12))
        poruka.place(x=20,y=30)
    root = Toplevel()
    root.title("PyFloraPosude")
    root.geometry("700x600+100+100")
    root.config(bg="#f5f6f2")
    root.resizable(False, False)

    slika_pozadine = PhotoImage(file="slike_za_gui\pozadina.png")
    pozadina = Label(root, image=slika_pozadine)
    pozadina.place(x=0, y=0)

    frame_naslov = Frame(root, bg="#f3edea", width=700, height=50)
    frame_naslov.place(x=0, y=0)
    naslov = Label(frame_naslov, text="PyFloraPosude", font=("Comic Sans MS", 16), bg="#f3edea")
    naslov.place(x=20, y=15)
    naslov1 = Label(root, text="Moj vrt", font=("Comic Sans MS", 16), bg="#f3edea")
    naslov1.place(x=300, y=60)

    def prva_posuda():
        def izlaz():
            okvir1.destroy()

        def dodijeli_biljku(senzor_vlage, senzor_temp, senzor_svjetla):
            
            naziv_biljke_za_prikaz = biljke_combo.get()
            
            if naziv_biljke_za_prikaz!="":
                conn = sqlite3.connect("PyFloraPosude.db")
                cursor = conn.cursor()

                cursor.execute("INSERT INTO Posude (lokacija, puna_prazna, naziv, vlaznost, temperatura, svjetlost) VALUES (?, ?, ?, ?, ?, ?)",
                    ("Posuda 1", "puna", naziv_biljke_za_prikaz,senzor_vlage , senzor_temp, senzor_svjetla))

                conn.commit()
                conn.close()
                prikazi_poruku("Unos biljaka", "Biljka je uspješno unesena u posudu!")
            else:
                prikazi_poruku("Unos biljaka", "Niste odabrali biljku za unos u posudu!")
              

        okvir1 = Frame(root, bg="#f3edea", width=190, height=390)
        okvir1.place(x=50, y=100)
        ukloni_biljku1 = Button(okvir1, text="x", command=izlaz)
        ukloni_biljku1.place(x=170, y=0)
        naslov_posude = Label(okvir1, text="Posuda 1", font=("Comic Sans MS", 12), bg="#f3edea")
        naslov_posude.place(x=70, y=10)

        conn = sqlite3.connect("PyFloraPosude.db")
        cursor = conn.cursor()
        cursor.execute("SELECT Naziv FROM Biljke")
        biljke = cursor.fetchall()
        conn.close()

        biljke_combo = ttk.Combobox(okvir1, font=("Comic Sans MS", 12), width=10)
        biljke_combo.place(x=40, y=40)
        biljke_list = [biljka[0] for biljka in biljke]
        biljke_combo['values'] = biljke_list
        

        biljke_combo.current(None)
       
             

        def generiraj_random_senzore():
            senzor_vlage = random.randint(20, 100)
            senzor_temp = random.randint(15, 30)
            senzor_svjetla = random.randint(1000, 10000)

            senzor_vlage_label = Label(okvir1, text=f"Senzor vlage: {senzor_vlage} %", font=("Comic Sans MS", 11), bg="#f3edea")
            senzor_vlage_label.place(x=5, y=140)

            senzor_temp_label = Label(okvir1, text=f"Senzor temp: {senzor_temp} °C", font=("Comic Sans MS", 11), bg="#f3edea")
            senzor_temp_label.place(x=5, y=170)

            senzor_svjetla_label = Label(okvir1, text=f"Senzor svjetla: {senzor_svjetla} Lux", font=("Comic Sans MS", 11), bg="#f3edea")
            senzor_svjetla_label.place(x=5, y=200)

            status=Label(okvir1, text="Status biljke:", font=("Comic Sans MS", 12), bg="#f3edea")
            status.place(x=5,y=270)
            generiraj_senzore_button = Button(okvir1, text="Dodjeli biljku posudi", bg="#a7c47a", width=15,height=1,font=("Comic Sans MS", 10), command=lambda: dodijeli_biljku(senzor_vlage, senzor_temp, senzor_svjetla))
            generiraj_senzore_button.place(x=20, y=230)
            
            if senzor_vlage>40 and senzor_vlage<70:
                status_vlage=Label(okvir1, text="Vlaga je OK!", fg="green",font=("Comic Sans MS", 11), bg="#f3edea")
                status_vlage.place(x=5,y=305)
            elif senzor_vlage>70 :
                status_vlage=Label(okvir1, text="Velika vlažnost tla!",fg="red", font=("Comic Sans MS", 11), bg="#f3edea")
                status_vlage.place(x=5,y=305)
            else:
                status_temp=Label(okvir1, text="Vlaga je niska!",fg="red", font=("Comic Sans MS", 11), bg="#f3edea")
                status_temp.place(x=5,y=305)

            if senzor_temp>=22 and senzor_temp<=25:
                status_temp=Label(okvir1, text="Temp je OK!", fg="green",font=("Comic Sans MS", 11), bg="#f3edea")
                status_temp.place(x=5,y=330)
            elif senzor_temp>25 :
                status_temp=Label(okvir1, text="Visoka temp!:",fg="red", font=("Comic Sans MS", 11), bg="#f3edea")
                status_temp.place(x=5,y=330)
            else:
                status_temp=Label(okvir1, text="Niska temp!",fg="red", font=("Comic Sans MS", 11), bg="#f3edea")
                status_temp.place(x=5,y=330)


            if senzor_svjetla>=4000 and senzor_svjetla<=7000:
                status_svjetla=Label(okvir1, text="Svjetlost je OK!", fg="green",font=("Comic Sans MS", 11), bg="#f3edea")
                status_svjetla.place(x=5,y=355)
            elif senzor_svjetla>7000:
                status_svjetla=Label(okvir1, text="Visoka razina svjetla!", fg="green",font=("Comic Sans MS", 11), bg="#f3edea")
                status_svjetla.place(x=5,y=355)
            else:
                status_svjetla=Label(okvir1, text="Niska razina svjetla!", fg="green",font=("Comic Sans MS", 11), bg="#f3edea")
                status_svjetla.place(x=5,y=355)
            
        generiraj_senzore_button = Button(okvir1, text="Generiraj senzore", bg="#a7c47a", width=15,height=1,font=("Comic Sans MS", 12), command=generiraj_random_senzore)
        generiraj_senzore_button.place(x=10, y=90)
    
    def druga_posuda():
        def izlaz():
            okvir2.destroy()

        def dodijeli_biljku(senzor_vlage, senzor_temp, senzor_svjetla):
            
            naziv_biljke_za_prikaz = biljke_combo.get()
            if naziv_biljke_za_prikaz!="":
                conn = sqlite3.connect("PyFloraPosude.db")
                cursor = conn.cursor()

                
                cursor.execute("INSERT INTO Posude (lokacija, puna_prazna, naziv, vlaznost, temperatura, svjetlost) VALUES (?, ?, ?, ?, ?, ?)",
                    ("Posuda 2", "puna", naziv_biljke_za_prikaz, senzor_vlage , senzor_temp, senzor_svjetla))

                conn.commit()
                conn.close()
                prikazi_poruku("Unos biljaka", "Biljka je uspješno unesena u posudu!")
            else:
                prikazi_poruku("Unos biljaka", "Niste odabrali biljku za unos u posudu!")
        
        okvir2 = Frame(root, bg="#f3edea", width=190, height=390)
        okvir2.place(x=260, y=100)
        ukloni_biljku1 = Button(okvir2, text="x", command=izlaz)
        ukloni_biljku1.place(x=170, y=0)
        naslov_posude = Label(okvir2, text="Posuda 2", font=("Comic Sans MS", 12), bg="#f3edea")
        naslov_posude.place(x=70, y=10)

        conn = sqlite3.connect("PyFloraPosude.db")
        cursor = conn.cursor()
        cursor.execute("SELECT Naziv FROM Biljke")
        biljke = cursor.fetchall()
        conn.close()

        biljke_combo = ttk.Combobox(okvir2, font=("Comic Sans MS", 12), width=10)
        biljke_combo.place(x=40, y=40)
        biljke_list = [biljka[0] for biljka in biljke]
        biljke_combo['values'] = biljke_list
        

        biljke_combo.current(None)
        
        def generiraj_random_senzore():
            senzor_vlage = random.randint(20, 100)
            senzor_temp = random.randint(15, 30)
            senzor_svjetla = random.randint(1000, 10000)

            senzor_vlage_label = Label(okvir2, text=f"Senzor vlage: {senzor_vlage} %", font=("Comic Sans MS", 11), bg="#f3edea")
            senzor_vlage_label.place(x=5, y=140)

            senzor_temp_label = Label(okvir2, text=f"Senzor temp: {senzor_temp} °C", font=("Comic Sans MS", 11), bg="#f3edea")
            senzor_temp_label.place(x=5, y=170)

            senzor_svjetla_label = Label(okvir2, text=f"Senzor svjetla: {senzor_svjetla} Lux", font=("Comic Sans MS", 11), bg="#f3edea")
            senzor_svjetla_label.place(x=5, y=200)

            status=Label(okvir2, text="Status biljke:", font=("Comic Sans MS", 12), bg="#f3edea")
            status.place(x=5,y=270)
            generiraj_senzore_button = Button(okvir2, text="Dodjeli biljku posudi", bg="#a7c47a", width=15,height=1,font=("Comic Sans MS", 10), command=lambda: dodijeli_biljku(senzor_vlage, senzor_temp, senzor_svjetla))
            generiraj_senzore_button.place(x=20,y=230)
            
            if senzor_vlage>=40 and senzor_vlage<=70:
                status_vlage=Label(okvir2, text="Vlaga je OK!", fg="green",font=("Comic Sans MS", 11), bg="#f3edea")
                status_vlage.place(x=5,y=305)
            elif senzor_vlage>70 :
                status_vlage=Label(okvir2, text="Velika vlažnost tla!:",fg="red", font=("Comic Sans MS", 11), bg="#f3edea")
                status_vlage.place(x=5,y=305)
            else:
                status_temp=Label(okvir2, text="Vlaga je niska!",fg="red", font=("Comic Sans MS", 11), bg="#f3edea")
                status_temp.place(x=5,y=305)

            if senzor_temp>=22 and senzor_temp<=25:
                status_temp=Label(okvir2, text="Temp je OK!", fg="green",font=("Comic Sans MS", 11), bg="#f3edea")
                status_temp.place(x=5,y=330)
            elif senzor_temp>25 :
                status_temp=Label(okvir2, text="Visoka temp!:",fg="red", font=("Comic Sans MS", 11), bg="#f3edea")
                status_temp.place(x=5,y=330)
            else:
                status_temp=Label(okvir2, text="Niska temp!",fg="red", font=("Comic Sans MS", 11), bg="#f3edea")
                status_temp.place(x=5,y=330)


            if senzor_svjetla>=4000 and senzor_svjetla<=7000:
                status_svjetla=Label(okvir2, text="Svjetlost je OK!", fg="green",font=("Comic Sans MS", 11), bg="#f3edea")
                status_svjetla.place(x=5,y=355)
            elif senzor_svjetla>7000:
                status_svjetla=Label(okvir2, text="Visoka razina svjetla!", fg="red",font=("Comic Sans MS", 11), bg="#f3edea")
                status_svjetla.place(x=5,y=355)
            else:
                status_svjetla=Label(okvir2, text="Niska razina svjetla!", fg="red",font=("Comic Sans MS", 11), bg="#f3edea")
                status_svjetla.place(x=5,y=355)
            
        generiraj_senzore_button = Button(okvir2, text="Generiraj senzore", bg="#a7c47a", width=15,height=1,font=("Comic Sans MS", 12), command=generiraj_random_senzore)
        generiraj_senzore_button.place(x=30, y=90)
    def treca_posuda():
        def izlaz():
            okvir3.destroy()

        def dodijeli_biljku(senzor_vlage, senzor_temp, senzor_svjetla):
            
            naziv_biljke_za_prikaz = biljke_combo.get()
            
            if naziv_biljke_za_prikaz!="":

                conn = sqlite3.connect("PyFloraPosude.db")
                cursor = conn.cursor()

                cursor.execute("INSERT INTO Posude (lokacija, puna_prazna, naziv, vlaznost, temperatura, svjetlost) VALUES (?, ?, ?, ?, ?, ?)",
                    ("Posuda 3", "puna", naziv_biljke_za_prikaz, senzor_vlage , senzor_temp, senzor_svjetla))

                conn.commit()
                conn.close()
                prikazi_poruku("Unos biljaka", "Biljka je uspješno unesena u posudu!")
            else:
                prikazi_poruku("Unos biljaka", "Niste odabrali biljku za unos u posudu!")
        

        okvir3 = Frame(root, bg="#f3edea", width=190, height=390)
        okvir3.place(x=470, y=100)
        ukloni_biljku1 = Button(okvir3, text="x", command=izlaz)
        ukloni_biljku1.place(x=170, y=0)
        naslov_posude = Label(okvir3, text="Posuda 3", font=("Comic Sans MS", 12), bg="#f3edea")
        naslov_posude.place(x=70, y=10)

        conn = sqlite3.connect("PyFloraPosude.db")
        cursor = conn.cursor()
        cursor.execute("SELECT Naziv FROM Biljke")
        biljke = cursor.fetchall()
        conn.close()

        biljke_combo = ttk.Combobox(okvir3, font=("Comic Sans MS", 12), width=10)
        biljke_combo.place(x=40, y=40)
        biljke_list = [biljka[0] for biljka in biljke]
        biljke_combo['values'] = biljke_list
    

        biljke_combo.current(None)
      
        def generiraj_random_senzore():
            senzor_vlage = random.randint(20, 100)
            senzor_temp = random.randint(15, 30)
            senzor_svjetla = random.randint(1000, 10000)

            senzor_vlage_label = Label(okvir3, text=f"Senzor vlage: {senzor_vlage} %", font=("Comic Sans MS", 11), bg="#f3edea")
            senzor_vlage_label.place(x=5, y=140)

            senzor_temp_label = Label(okvir3, text=f"Senzor temp: {senzor_temp} °C", font=("Comic Sans MS", 11), bg="#f3edea")
            senzor_temp_label.place(x=5, y=170)

            senzor_svjetla_label = Label(okvir3, text=f"Senzor svjetla: {senzor_svjetla} Lux", font=("Comic Sans MS", 11), bg="#f3edea")
            senzor_svjetla_label.place(x=5, y=200)

            status=Label(okvir3, text="Status biljke:", font=("Comic Sans MS", 12), bg="#f3edea")
            status.place(x=5,y=270)
            generiraj_senzore_button = Button(okvir3, text="Dodjeli biljku posudi", bg="#a7c47a", width=15,height=1,font=("Comic Sans MS", 10), command=lambda: dodijeli_biljku(senzor_vlage, senzor_temp, senzor_svjetla))
            generiraj_senzore_button.place(x=20, y=230)
            
            if senzor_vlage>=40 and senzor_vlage<=70:
                status_vlage=Label(okvir3, text="Vlaga je OK!", fg="green",font=("Comic Sans MS", 11), bg="#f3edea")
                status_vlage.place(x=5,y=305)
            elif senzor_vlage>70 :
                status_vlage=Label(okvir3, text="Velika vlažnost tla!:",fg="red", font=("Comic Sans MS", 11), bg="#f3edea")
                status_vlage.place(x=5,y=305)
            else:
                status_vlaga=Label(okvir3, text="Vlaga je niska!",fg="red", font=("Comic Sans MS", 11), bg="#f3edea")
                status_vlaga.place(x=5,y=305)

            if senzor_temp>=22 and senzor_temp<=25:
                status_temp=Label(okvir3, text="Temp je OK!", fg="green",font=("Comic Sans MS", 11), bg="#f3edea")
                status_temp.place(x=5,y=330)
            elif senzor_temp>25 :
                status_temp=Label(okvir3, text="Visoka temp!:",fg="red", font=("Comic Sans MS", 11), bg="#f3edea")
                status_temp.place(x=5,y=330)
            else:
                status_temp=Label(okvir3, text="Niska temp!",fg="red", font=("Comic Sans MS", 11), bg="#f3edea")
                status_temp.place(x=5,y=330)


            if senzor_svjetla>=4000 and senzor_svjetla<=7000:
                status_svjetla=Label(okvir3, text="Svjetlost je OK!", fg="green",font=("Comic Sans MS", 11), bg="#f3edea")
                status_svjetla.place(x=5,y=355)
            elif senzor_svjetla>7000:
                status_svjetla=Label(okvir3, text="Visoka razina svjetla!", fg="red",font=("Comic Sans MS", 11), bg="#f3edea")
                status_svjetla.place(x=5,y=355)
            else:
                status_svjetla=Label(okvir3, text="Niska razina svjetla!", fg="red",font=("Comic Sans MS", 11), bg="#f3edea")
                status_svjetla.place(x=5,y=355)
            
        generiraj_senzore_button = Button(okvir3, text="Generiraj senzore", bg="#a7c47a", width=15,height=1,font=("Comic Sans MS", 12), command=generiraj_random_senzore)
        generiraj_senzore_button.place(x=10, y=90)

    slika_posuda=PhotoImage(file="slike_za_gui\pot.png").subsample(2)    
    dodaj_posudu1 = Button(root, text="",image=slika_posuda,compound=CENTER,bg="#f3edea",width=180,height=155, command=prva_posuda)
    dodaj_posudu1.place(x=50, y=100)
    dodaj_posudu2 = Button(root, text="", image=slika_posuda, compound=CENTER, font=("Comic Sans MS", 16), bg="#f3edea", width=180, height=155, command=druga_posuda)
    dodaj_posudu2.place(x=260, y=100)
    dodaj_posudu3 = Button(root, text="", image=slika_posuda, compound=CENTER, font=("Comic Sans MS", 16), bg="#f3edea", width=180, height=155,command=treca_posuda)
    dodaj_posudu3.place(x=470, y=100)
    root.mainloop()
