from tkinter import*
from tkinter import ttk
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def grafikoni():    
    def prikazi_podatke_o_biljci():
        odabrana_biljka = biljka_combo.get()
        
        conn = sqlite3.connect("PyFloraPosude.db")
        cursor = conn.cursor()
        
        cursor.execute("SELECT temperatura, vlaznost, svjetlost FROM Posude WHERE naziv=?", (odabrana_biljka,))
        
        podaci = cursor.fetchall()
        
        conn.close()
        
        
        temperatura = [podatak[0] for podatak in podaci]
        vlaznost = [podatak[1] for podatak in podaci]
        svjetlost = [podatak[2] for podatak in podaci]
        

        ax_temp.clear()
        ax_humidity.clear()
        ax_light.clear()

        ax_temp.plot(temperatura, marker='o', linestyle='-')
        ax_temp.set_title('Graf temperature')
        ax_temp.set_xlabel('Vrijeme',fontdict={'fontname': 'Comic Sans MS', 'fontsize': 8})
        ax_temp.set_ylabel('Temperatura (°C)',fontdict={'fontname': 'Comic Sans MS', 'fontsize': 8})


        ax_humidity.bar(range(len(vlaznost)), vlaznost, tick_label=range(len(vlaznost)))
        ax_humidity.set_title('Stupčasti graf vlažnosti')
        ax_humidity.set_xlabel('Vrijeme',fontdict={'fontname': 'Comic Sans MS', 'fontsize': 8})
        ax_humidity.set_ylabel('Vlažnost (%)',fontdict={'fontname': 'Comic Sans MS', 'fontsize': 8})

        ax_light.plot(svjetlost, marker='o', linestyle='-')
        ax_light.set_title('Graf svjetlosti')
        ax_light.set_xlabel('Vrijeme',fontdict={'fontname': 'Comic Sans MS', 'fontsize': 8})
        ax_light.set_ylabel('Svjetlost (lux)',fontdict={'fontname': 'Comic Sans MS', 'fontsize': 8})

        canvas_temp.draw()
        canvas_humidity.draw()
        canvas_light.draw()


    root6 = Toplevel()
    root6.title("PyFloraPosude")
    root6.geometry("700x600+100+100")
    root6.config(bg="#f5f6f2")
    root6.resizable(False, False)

    slika_pozadine = PhotoImage(file="slike_za_gui\pozadina.png")
    pozadina = Label(root6, image=slika_pozadine)
    pozadina.place(x=0, y=0)

    frame_naslov = Frame(root6, bg="#f3edea", width=700, height=50)
    frame_naslov.place(x=0, y=0)
    naslov = Label(frame_naslov, text="PyFloraPosude", font=("Comic Sans MS", 16), bg="#f3edea")
    naslov.place(x=20, y=15)
    naslov_korisnici = Label(root6, text="Grafički prikaz", font=("Comic Sans MS", 16), bg="#f3edea")
    naslov_korisnici.place(x=250, y=30)


    # Stvaranje grafova za temperaturu, vlažnost i svjetlost
    fig_temp = plt.Figure(figsize=(2.2,2.2),dpi=100)
    fig_humidity = plt.Figure(figsize=(2.2, 2.2), dpi=100)
    fig_light = plt.Figure(figsize=(2.2, 2.2), dpi=100)

    # Postavljanje grafova u Tkinter prozor
    canvas_temp = FigureCanvasTkAgg(fig_temp, master=root6)
    canvas_temp.get_tk_widget().place(x=20, y=200)

    canvas_humidity = FigureCanvasTkAgg(fig_humidity, master=root6)
    canvas_humidity.get_tk_widget().place(x=250, y=200)

    canvas_light = FigureCanvasTkAgg(fig_light, master=root6)
    canvas_light.get_tk_widget().place(x=480, y=200)

    conn = sqlite3.connect("PyFloraPosude.db")
    cursor = conn.cursor()
    cursor.execute("SELECT Naziv FROM Biljke")
    biljke = cursor.fetchall()
    conn.close()

    biljka_combo = ttk.Combobox(root6, values=[biljka[0] for biljka in biljke])
    biljka_combo.place(x=100, y=100)

    gumb_prikazi = Button(root6, text="Prikaži podatke", bg="#a7c47a", font=("Comic Sans MS", 12), width=15, command=prikazi_podatke_o_biljci)
    gumb_prikazi.place(x=250, y=100)

    ax_temp = fig_temp.add_subplot(111)
    ax_humidity = fig_humidity.add_subplot(111)
    ax_light = fig_light.add_subplot(111)

    root6.mainloop()

