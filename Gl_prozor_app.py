from tkinter import*
from moj_vrt import prijava_moj_vrt
from vrem_prognoza import vremenska_prognoza
from korisnici import korisnici_update
from grafovi import grafikoni
import subprocess

def prijava_u_gl_prozor(ime_korisnika, prezime_korisnika, status_korisnika):
        profilna_slika=PhotoImage(file="slike_za_gui\profilna_slika.png").subsample(2)
        def log_out():
                root1.destroy()
        def moj_profil():
                def izlaz():
                        okvir_profila.destroy()
                okvir_profila=Frame(root1, bg="#f3edea", width=640, height=300)
                okvir_profila.place(x=50,y=80)
                slika_profila=Label(okvir_profila,image=profilna_slika)
                slika_profila.place(x=0,y=100)
                ime_fiksno=Label(okvir_profila, text="Ime:", font=("Comic Sans MS",16),bg="#f3edea")
                ime_fiksno.place(x=150,y=100)
                ime_profil=Label(okvir_profila, text=f"{ime_korisnika}", font=("Comic Sans MS",16),bg="#f3edea")
                ime_profil.place(x=210,y=100)
                prezime_fiksno=Label(okvir_profila, text="Prezime:", font=("Comic Sans MS",16),bg="#f3edea")
                prezime_fiksno.place(x=150,y=150)
                prezime_profil=Label(okvir_profila, text=f"{prezime_korisnika}", font=("Comic Sans MS",16),bg="#f3edea")
                prezime_profil.place(x=250,y=150)
                status_fiksno=Label(okvir_profila, text="Status korisnika:", font=("Comic Sans MS",16),bg="#f3edea")
                status_fiksno.place(x=150,y=200)
                status_profila=Label(okvir_profila, text=f"{status_korisnika}", font=("Comic Sans MS",16),bg="#f3edea")
                status_profila.place(x=330,y=200)
                izlaz_iz_profila=Button(okvir_profila, text="X", bg="#a7c47a", font=("Comic Sans MS",10),width=5,command=izlaz)
                izlaz_iz_profila.place(x=550,y=10)
                
        def moj_vrt():
                prijava_moj_vrt()
        def prikaz_graf():
                grafikoni()
        def moje_biljke():
                subprocess.run(["python", "moje_biljke.py"])
        def vremenska_prognoza_gumb():
                vremenska_prognoza()

        root1=Toplevel()
        root1.title("PyFloraPosude")
        root1.geometry()
        root1.geometry("700x600+100+100")
        root1.config(bg="#f5f6f2")
        root1.resizable(False, False)

        slika_pozadine=PhotoImage(file="slike_za_gui\pozadina.png")
        pozadina=Label(root1, image=slika_pozadine)
        pozadina.place(x=0,y=0)

        frame_naslov=Frame(root1, bg="#f3edea", width=700 ,height=50)
        frame_naslov.place(x=0,y=0)
        naslov=Label(frame_naslov, text="PyFloraPosude", font=("Comic Sans MS",16),bg="#f3edea")
        naslov.place(x=20,y=15)
     
        label_ime_korisnika = Label(root1, text=f"Prijavljeni korisnik: {ime_korisnika} {prezime_korisnika}", font=("Comic Sans MS", 11), bg="#f3edea")
        label_ime_korisnika.place(x=440, y=20)
        moj_prof=Button(root1, text="Moj profil", bg="#a7c47a", font=("Comic Sans MS",10),width=10,command=moj_profil)
        moj_prof.place(x=540,y=50)
        logout=Button(root1, text="Logout", bg="#a7c47a", font=("Comic Sans MS",10),width=5,command=log_out)
        logout.place(x=640,y=50)

        gumb1_slika=PhotoImage(file="slike_za_gui\my_plants.png").subsample(2)
        gumb1=Button(root1, image=gumb1_slika,command=moj_vrt)
        gumb1.place(x=90,y=160)
        moj_vrt_tekst=Label(root1, text="Moj vrt",font=("Comic Sans MS",16),bg="#f3edea")
        moj_vrt_tekst.place(x=110,y=300)

        gumb2_slika=PhotoImage(file="slike_za_gui\graf.png").subsample(2)
        gumb2=Button(root1, image=gumb2_slika,command=prikaz_graf)
        gumb2.place(x=230,y=160)
        grafikoni_tekst=Label(root1, text="Grafikoni",font=("Comic Sans MS",16),bg="#f3edea")
        grafikoni_tekst.place(x=250,y=300)

        gumb3_slika=PhotoImage(file="slike_za_gui\plant.png").subsample(2)
        gumb3=Button(root1, image=gumb3_slika, command=moje_biljke)
        gumb3.place(x=370,y=160)
        moje_biljke_tekst=Label(root1, text="Moje biljke",font=("Comic Sans MS",16),bg="#f3edea")
        moje_biljke_tekst.place(x=380,y=300)

        gumb4_slika=PhotoImage(file="slike_za_gui\prognoza.png").subsample(2)
        gumb4=Button(root1, image=gumb4_slika,command=vremenska_prognoza_gumb)
        gumb4.place(x=510,y=160)
        vremenska_tekst=Label(root1, text="Vremenska",font=("Comic Sans MS",16),bg="#f3edea")
        vremenska_tekst.place(x=520,y=300)
        prognoza_tekst=Label(root1, text="prognoza",font=("Comic Sans MS",16),bg="#f3edea")
        prognoza_tekst.place(x=530,y=330)

        def uredi_korisnike():
                korisnici_update()


        if status_korisnika=="administrator" or status_korisnika=="admin":
                        uredivanje_korisnika=Button(root1, text="Uredi korisnike", bg="#a7c47a", font=("Comic Sans MS",10),width=15, command=uredi_korisnike)
                        uredivanje_korisnika.place(x=550,y=90)
           
        root1.mainloop()
