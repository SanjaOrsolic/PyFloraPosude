from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import io
from PIL import Image, ImageTk
import sqlite3


    
def prikazi_poruku(naslov, poruka):
    dialog = Toplevel(root4)
    dialog.geometry("400x100+100+100")
    dialog.config(bg="#f5f6f2")
    dialog.title(naslov)
    poruka=Label(dialog, text=poruka, bg="#f5f6f2", font=("Comic Sans MS", 12))
    poruka.place(x=10,y=30)

def prikazi_frame(frame):
    nova_biljka_frame.place_forget()
    azuriranje_biljka_frame.place_forget()
    brisanje_biljka_frame.place_forget()
    pregled_biljka_frame.place_forget()
        
def dodaj_novu_biljku():
    prikazi_frame(nova_biljka_frame)
    nova_biljka_frame.place(x=150, y=140)

def azuriraj_biljku():
    prikazi_frame(azuriranje_biljka_frame)
    azuriranje_biljka_frame.place(x=150, y=140)
    
    conn = sqlite3.connect("PyFloraPosude.db")
    cursor = conn.cursor()
    cursor.execute("SELECT Naziv FROM Biljke")
    biljke = cursor.fetchall()
    conn.close()

    biljke_list = [biljka[0] for biljka in biljke]
    biljke_combo['values'] = biljke_list
    biljke_combo.current(0)  
        
def odaberi_sliku_za_azuriranje():
    global odabrana_slika_path
    odabrana_slika_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")])
    if odabrana_slika_path:
        # Prikaži odabranu sliku
        image = Image.open(odabrana_slika_path)
        image.thumbnail((100, 100))  
        photo = ImageTk.PhotoImage(image)
        slika_label_azu.config(image=photo)
        slika_label_azu.image = photo
   
def unesi_izmjene():
    global odabrana_slika_path
    naziv_novi = unos_naziva_entry_azuriranje.get()
    biljka_za_azuriranje = biljke_combo.get()
    min_azu_temp=min_temp_azu.get()
    max_azu_temp=max_temp_azu.get()
    ideal_azu_vlaga=ideal_vlaga_azu.get()
    ideal_azu_svjetlo=ideal_svjetlo_azu.get()
    if naziv_novi and biljka_za_azuriranje and min_azu_temp and max_azu_temp and ideal_azu_vlaga and ideal_azu_svjetlo:
        conn = sqlite3.connect("PyFloraPosude.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE Biljke SET Naziv=? WHERE Naziv=?", (naziv_novi,biljka_za_azuriranje))
          
        if odabrana_slika_path:
            with open(odabrana_slika_path, "rb") as image_file:
                image_blob = image_file.read()
            cursor.execute("UPDATE Biljke SET Slika=? WHERE Naziv=?", (image_blob, naziv_novi))
            slika_label_azu.config(image=None)
            slika_label_azu.image = None
        cursor.execute("UPDATE Biljke SET Ideal_min_temp=?, Ideal_max_temp=?, Ideal_vlaznost=?, Ideal_svjetlost=? WHERE Naziv=?", (min_azu_temp, max_azu_temp, ideal_azu_vlaga, ideal_azu_svjetlo, naziv_novi))
        conn.commit()
        conn.close()
        prikazi_poruku("Ažuriranje", "Biljka je uspješno ažurirana!")
                                  
    else:
        prikazi_poruku("Upozorenje", "Popunite sva polja kako bi uspješno ažurirali biljku!")
    unos_naziva_entry.delete(0,END)
    biljke_combo.delete(0,END)
    min_temp_azu.delete(0,END)
    max_temp_azu.delete(0,END)
    ideal_vlaga_azu.delete(0,END)
    ideal_svjetlo_azu.delete(0,END)
    slika_label_azu.destroy()
    odabrana_slika_path = ""
        
        

def brisanje_biljke():
    prikazi_frame(brisanje_biljka_frame)
    brisanje_biljka_frame.place(x=150, y=150)
    
    conn = sqlite3.connect("PyFloraPosude.db")
    cursor = conn.cursor()
    cursor.execute("SELECT Naziv FROM Biljke")
    biljke = cursor.fetchall()
    conn.close()

    biljke_list_brisanje = [biljka[0] for biljka in biljke]
    biljke_combo_brisanje['values'] = biljke_list_brisanje
    biljke_combo_brisanje.set("")  

def obrisi_biljku():
    biljka_za_brisanje = biljke_combo_brisanje.get()
    if biljka_za_brisanje:
        conn = sqlite3.connect("PyFloraPosude.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Biljke WHERE Naziv=?", (biljka_za_brisanje,))
        conn.commit()
        conn.close()
        prikazi_poruku("Brisanje", "Biljka je uspješno obrisana!")
    else:
        prikazi_poruku("Upozorenje", "Odaberite biljku za brisanje!")
    biljke_combo_brisanje.delete(0,END)
def prikaz_biljki():
    prikazi_frame(pregled_biljka_frame)
    pregled_biljka_frame.place(x=150, y=150)
        
    conn = sqlite3.connect("PyFloraPosude.db")
    cursor = conn.cursor()
    cursor.execute("SELECT Naziv FROM Biljke")
    biljke = cursor.fetchall()
    conn.close()

    biljke_list_prikaz = [biljka[0] for biljka in biljke]
    biljke_combo_prikaz['values'] = biljke_list_prikaz

def prikazi_odabrane_biljke():
    naziv_biljke_za_prikaz = biljke_combo_prikaz.get()
    if naziv_biljke_za_prikaz:
        conn = sqlite3.connect("PyFloraPosude.db")
        cursor = conn.cursor()
        cursor.execute("SELECT Slika FROM Biljke WHERE Naziv=?", (naziv_biljke_za_prikaz,))
        slika_blob = cursor.fetchone()
        cursor.execute("SELECT * FROM Biljke WHERE Naziv=?", (naziv_biljke_za_prikaz,))
        info_biljke=cursor.fetchone()
        conn.close()

        info_za_prikaz=Label(pregled_biljka_frame, text=f"Naziv:  {info_biljke[1]}\nMin temperatura:  {info_biljke[5]}\nMax temperatura:  {info_biljke[4]}\nIdealna vlažnost:  {info_biljke[3]}\nIdealna svjetlost:  {info_biljke[6]}",font=("Comic Sans MS", 12), bg="#f3edea",justify="left")    
        info_za_prikaz.place(x=20,y=160)
            
        if slika_blob:
            slika = Image.open(io.BytesIO(slika_blob[0]))
            slika.thumbnail((150, 150))  
            photo = ImageTk.PhotoImage(slika)
            slika_label_prikaz.config(image=photo)
            slika_label_prikaz.image = photo
        else:
            prikazi_poruku("Upozorenje", "Nema dostupne slike za prikaz!")
            
def odaberi_sliku():
        
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")])
    if file_path:
        image = Image.open(file_path)
        image.thumbnail((100, 100))  
        photo = ImageTk.PhotoImage(image)
        slika_label1.config(image=photo)
        slika_label1.image = photo
        global odabrana_slika_path
        odabrana_slika_path = file_path

def unesi_biljku():
    global odabrana_slika_path
    naziv_biljke = unos_naziva_entry.get()
    idealna_vlaznost=ideal_vlaga.get()
    maximum_temp=max_temp.get()
    minimum_temp=min_temp.get()
    idealno_svjetlo=ideal_svjetlo.get()
    if naziv_biljke and odabrana_slika_path and idealna_vlaznost and maximum_temp and minimum_temp and idealno_svjetlo:
        conn = sqlite3.connect("PyFloraPosude.db")
        cursor = conn.cursor()
        with open(odabrana_slika_path, "rb") as image_file:
            image_blob = image_file.read()
        cursor.execute("INSERT INTO Biljke (Naziv, Slika, Ideal_vlaznost, ideal_max_temp, ideal_min_temp, ideal_svjetlost) VALUES (?, ?, ?, ?, ?, ?)", (naziv_biljke, image_blob,idealna_vlaznost,maximum_temp,minimum_temp,idealno_svjetlo))
        conn.commit()
        conn.close()
        prikazi_poruku("Unos", "Biljka je uspješno unesena u bazu!")
            
        odabrana_slika_path = ""
            
        slika_label1.config(image=None)
        slika_label1.image = None
    else:
        prikazi_poruku("Upozorenje", "Popunite sva polja za unos nove biljke!")
    unos_naziva_entry.delete(0,END)
    ideal_vlaga.delete(0,END)
    ideal_svjetlo.delete(0,END)
    max_temp.delete(0,END)
    min_temp.delete(0,END)
        

        
        

root4 = Tk()
root4.title("PyFloraPosude")
root4.geometry("700x600+100+100")
root4.config(bg="#f5f6f2")
root4.resizable(False, False)

slika_pozadine = PhotoImage(file="slike_za_gui\pozadina.png")
pozadina = Label(root4, image=slika_pozadine)
pozadina.place(x=0, y=0)

frame_naslov = Frame(root4, bg="#f3edea", width=700, height=50)
frame_naslov.place(x=0, y=0)
naslov = Label(frame_naslov, text="PyFloraPosude", font=("Comic Sans MS", 16), bg="#f3edea")
naslov.place(x=20, y=15)
naslov1 = Label(root4, text="Moje biljke", font=("Comic Sans MS", 16), bg="#f3edea")
naslov1.place(x=300, y=60)

nova_biljka_frame = Frame(root4, bg="#f3edea", width=400, height=380)

azuriranje_biljka_frame = Frame(root4, bg="#f3edea", width=400, height=400)

brisanje_biljka_frame = Frame(root4, bg="#f3edea", width=400, height=300)

pregled_biljka_frame = Frame(root4, bg="#f3edea", width=500, height=300)


    # Frame za dodavanje nove biljke
naslov_nova=Label(nova_biljka_frame,text="Unos nove biljke",font=("Comic Sans MS", 16), bg="#f3edea")
naslov_nova.place(x=100,y=0)
unos_naziva_label = Label(nova_biljka_frame, text="Unesite naziv biljke:", font=("Comic Sans MS", 12), bg="#f3edea")
unos_naziva_label.place(x=10,y=40)
unos_naziva_entry = Entry(nova_biljka_frame, font=("Comic Sans MS", 12),width=10)
unos_naziva_entry.place(x=180,y=40)

ideal_min_temp=Label(nova_biljka_frame, text="Minimalna temperatura: ", font=("Comic Sans MS", 12), bg="#f3edea")
ideal_min_temp.place(x=10,y=80)
min_temp=Entry(nova_biljka_frame, font=("Comic Sans MS", 12),width=5)
min_temp.place(x=220,y=80)
ideal_max_temp=Label(nova_biljka_frame, text="Maksimalna temperatura: ", font=("Comic Sans MS", 12), bg="#f3edea")
ideal_max_temp.place(x=10,y=120)
max_temp=Entry(nova_biljka_frame, font=("Comic Sans MS", 12),width=5)
max_temp.place(x=220,y=120)
ideal_vlaga_txt=Label(nova_biljka_frame, text="Idealna vlaga: ", font=("Comic Sans MS", 12), bg="#f3edea")
ideal_vlaga_txt.place(x=10,y=160)
ideal_svjetlo_txt=Label(nova_biljka_frame, text="Idealna svjetlost: ", font=("Comic Sans MS", 12), bg="#f3edea")
ideal_svjetlo_txt.place(x=220,y=160)

ideal_vlaga = ttk.Combobox(nova_biljka_frame, font=("Comic Sans MS", 12),width=12)
ideal_vlaga.place(x=10,y=190)
ideal_vlaga['values'] = ("Niska vlaga","Umjerena vlaga" ,"Visoka vlaga") 
    
ideal_svjetlo = ttk.Combobox(nova_biljka_frame, font=("Comic Sans MS", 12),width=12)
ideal_svjetlo.place(x=220,y=190)
ideal_svjetlo['values'] = ("Tamno mjesto","Polusvjetlo" ,"Puno svjetlosti")   

odabir_slike_button = Button(nova_biljka_frame, text="Odaberi sliku", bg="#a7c47a", font=("Comic Sans MS", 12), command=odaberi_sliku)
odabir_slike_button.place(x=20,y=230)

slika_frame = Frame(nova_biljka_frame, bg="#f3edea")
slika_frame.place(x=20,y=275)
slika_label1 = Label(slika_frame)
slika_label1.pack()
unesi_button = Button(nova_biljka_frame, text="Unesi biljku u bazu", bg="#a7c47a", font=("Comic Sans MS", 12), command=unesi_biljku)
unesi_button.place(x=200,y=230)


    # Frame za ažuriranje biljke
naslov_azuriranje=Label(azuriranje_biljka_frame,text="Ažuriranje biljke",font=("Comic Sans MS", 16), bg="#f3edea")
naslov_azuriranje.place(x=100,y=0)
biljke_combo = ttk.Combobox(azuriranje_biljka_frame, font=("Comic Sans MS", 12),width=15)
biljke_combo.place(x=100,y=40)
unos_naziva_label = Label(azuriranje_biljka_frame, text="Unesite naziv biljke:", font=("Comic Sans MS", 12), bg="#f3edea")
unos_naziva_label.place(x=10,y=80)
unos_naziva_entry_azuriranje = Entry(azuriranje_biljka_frame, font=("Comic Sans MS", 12),width=15)
unos_naziva_entry_azuriranje.place(x=190,y=80)

ideal_min_temp_azu=Label(azuriranje_biljka_frame, text="Minimalna temperatura: ", font=("Comic Sans MS", 12), bg="#f3edea")
ideal_min_temp_azu.place(x=10,y=110)
min_temp_azu=Entry(azuriranje_biljka_frame, font=("Comic Sans MS", 12),width=5)
min_temp_azu.place(x=220,y=110)
ideal_max_temp_azu=Label(azuriranje_biljka_frame, text="Maksimalna temperatura: ", font=("Comic Sans MS", 12), bg="#f3edea")
ideal_max_temp_azu.place(x=10,y=150)
max_temp_azu=Entry(azuriranje_biljka_frame, font=("Comic Sans MS", 12),width=5)
max_temp_azu.place(x=220,y=150)
ideal_vlaga_txt_azu=Label(azuriranje_biljka_frame, text="Idealna vlaga: ", font=("Comic Sans MS", 12), bg="#f3edea")
ideal_vlaga_txt_azu.place(x=10,y=180)
ideal_svjetlo_txt_azu=Label(azuriranje_biljka_frame, text="Idealna svjetlost: ", font=("Comic Sans MS", 12), bg="#f3edea")
ideal_svjetlo_txt_azu.place(x=220,y=180)

ideal_vlaga_azu= ttk.Combobox(azuriranje_biljka_frame, font=("Comic Sans MS", 12),width=12)
ideal_vlaga_azu.place(x=10,y=210)
ideal_vlaga_azu['values'] = ("Niska vlaga","Umjerena vlaga" ,"Visoka vlaga") 
    
ideal_svjetlo_azu = ttk.Combobox(azuriranje_biljka_frame, font=("Comic Sans MS", 12),width=12)
ideal_svjetlo_azu.place(x=220,y=210)
ideal_svjetlo_azu['values'] = ("Tamno mjesto","Polusvjetlo" ,"Puno svjetlosti")

odabir_slike_button_azu = Button(azuriranje_biljka_frame,text="Odaberi sliku", bg="#a7c47a", font=("Comic Sans MS", 12), command=odaberi_sliku_za_azuriranje)
odabir_slike_button_azu.place(x=20,y=250)
slika_frame_azu = Frame(azuriranje_biljka_frame, bg="#f3edea")
slika_frame_azu.place(x=20,y=295)
slika_label_azu = Label(slika_frame_azu)
slika_label_azu.pack()
unesi_izmjene_button = Button(azuriranje_biljka_frame, text="Unesi izmjene", bg="#a7c47a", font=("Comic Sans MS", 12), command=unesi_izmjene)
unesi_izmjene_button.place(x=200,y=250)
    
 # Frame za brisanje biljke
naslov_brisanje=Label(brisanje_biljka_frame,text="Brisanje biljke",font=("Comic Sans MS", 16), bg="#f3edea")
naslov_brisanje.place(x=120,y=0)
biljke_combo_brisanje = ttk.Combobox(brisanje_biljka_frame, font=("Comic Sans MS", 12))
biljke_combo_brisanje.place(x=70,y=60)
obrisi_button = Button(brisanje_biljka_frame, text="Obriši", bg="#a7c47a", font=("Comic Sans MS", 12), command=obrisi_biljku)
obrisi_button.place(x=150,y=120)

    # Frame za pregled biljke
naslov_pregled=Label(pregled_biljka_frame,text="Prikaz biljke",font=("Comic Sans MS", 16), bg="#f3edea")
naslov_pregled.place(x=120,y=0)
biljke_combo_prikaz = ttk.Combobox(pregled_biljka_frame, font=("Comic Sans MS", 12))
biljke_combo_prikaz.place(x=70,y=50)
prikazi_button = Button(pregled_biljka_frame, text="Prikaži", bg="#a7c47a", font=("Comic Sans MS", 12), command=prikazi_odabrane_biljke)
prikazi_button.place(x=140,y=100)
slika_label_prikaz = Label(pregled_biljka_frame)
slika_label_prikaz.place(x=320,y=120)


    # Glavni gumbi
nova_bilj = Button(root4, text="Nova biljka", bg="#a7c47a", font=("Comic Sans MS", 12), command=dodaj_novu_biljku)
nova_bilj.place(x=90, y=100)
azuriranje_bilj = Button(root4, text="Ažuriranje biljki", bg="#a7c47a", font=("Comic Sans MS", 12), command=azuriraj_biljku)
azuriranje_bilj.place(x=210, y=100)
brisanje_bilj = Button(root4, text="Brisanje biljki", bg="#a7c47a", font=("Comic Sans MS", 12), command=brisanje_biljke)
brisanje_bilj.place(x=360, y=100)
pregled_bilj = Button(root4, text="Pregled biljki", bg="#a7c47a", font=("Comic Sans MS", 12), command=prikaz_biljki)
pregled_bilj.place(x=490, y=100)

root4.mainloop()