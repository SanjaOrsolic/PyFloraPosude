from tkinter import*
import datetime as dt
import locale
import requests
import json

def vremenska_prognoza():
        def get_weather_data(api_key, city_id):  
            api_url = "http://api.openweathermap.org/data/2.5/weather"  
            params = {  
                "id": city_id,  
                "units": "metric",  
                "appid": api_key  
            }  
            response = requests.get(api_url, params=params)  
            data = response.json()  
            return data  
        
        api_key = "c94a2499bf7fc730cc0e2d7777112526"  
        city_id = "3186294"  # Žu 
        
        podaci = get_weather_data(api_key, city_id)  
                
        temperature = podaci["main"]["temp"]  
        city = podaci["name"]  
        humidity = podaci["main"]["humidity"]  
        wind_speed = podaci["wind"]["speed"]
        vrijeme_ikona=podaci['weather'][0]['description']
        
        import time  
        import threading  
        
        def get_hourly_weather_data():  
            while True:  
                data = get_weather_data(api_key, city_id)  
                time.sleep(3600)  # wait one hour  
        
        thread = threading.Thread(target=get_hourly_weather_data)  
        thread.start()


        filename_json = 'weather_Zu.json'
        with open(filename_json, 'w') as file:
            json.dump(podaci, file, indent=4)


        #-------GUI


        root=Toplevel()
        root.title("PyFloraPosude")
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
        naslov_2=Label(root, text="Vremenska prognoza", font=("Comic Sans MS",16),bg="#f3edea")
        naslov_2.place(x=250,y=80)


        #-----Datum i vrijeme
        locale.setlocale(locale.LC_TIME, 'hr_HR')
        datum=dt.datetime.now()
        lijepi_datum=datum.strftime("%d. %B %Y.")
        dan=datum.strftime("%A")
        dan_prikaz=dan.capitalize()

        def vrijeme():
            sat=time.strftime("%H:%M:%S")
            sat_prikaz=Label(root, text=sat, font=("Comic Sans MS", 24),bg="#f3edea",padx=10)
            sat_prikaz.place(x=50, y=210)
            root.after(1000,vrijeme)
        vrijeme()

        #-----Datum i vrijeme GUI
        datum_prikaz=Label(root, text=(f"{dan_prikaz},  {lijepi_datum}"), font=("Comic Sans MS", 14), bg="#f3edea")
        datum_prikaz.place(x=20,y=150)



        #----- Temperatura i vrijeme GUI
        grad=Label(root, text=f"{city} ",font=("Comic Sans MS", 16),  bg="#f3edea")
        grad.place(x=400,y=150)
        temp_text=Label(root,text="Temperatura:",font=("Comic Sans MS", 12),  bg="#f3edea")
        temp_text.place(x=530,y=170)
        temp_prikaz=Label(root,text=f"{round(temperature)} °C",font=("Comic Sans MS", 18),  bg="#f3edea")
        temp_prikaz.place(x=610,y=195)
        tlak_zraka_text=Label(root,text="Brzina vjetra:",font=("Comic Sans MS", 12), bg="#f3edea")
        tlak_zraka_text.place(x=530,y=230)
        brzina_vjetra_prikaz=Label(root,text=f"{round(wind_speed,1)} m/s",font=("Comic Sans MS", 14),  bg="#f3edea")
        brzina_vjetra_prikaz.place(x=610,y=260)
        vlaznost_text=Label(root,text="Vlaznost:",font=("Comic Sans MS", 12), bg="#f3edea")
        vlaznost_text.place(x=530,y=300)
        vlaznost_prikaz=Label(root,text=f"{round(humidity)} %",font=("Comic Sans MS", 14), bg="#f3edea")
        vlaznost_prikaz.place(x=610,y=330)


        if vrijeme_ikona=="few clouds" or vrijeme_ikona=="scattered clouds":
            few_clouds=PhotoImage(file="slike_za_gui\few_clouds.png").subsample(30)
            few_clouds_prikaz=Label(root, image=few_clouds,bg="#f3edea")
            few_clouds_prikaz.place(x=350,y=190)
        elif vrijeme_ikona=="clear sky":
            clear_sky=PhotoImage(file="slike_za_gui\clear_sky.png").subsample(3)
            clear_sky_prikaz=Label(root, image=clear_sky,bg="#f3edea")
            clear_sky_prikaz.place(x=350,y=190)
        elif vrijeme_ikona=="moderate rain" or vrijeme_ikona=="light rain" or vrijeme_ikona=="heavy intensity rain":
            rain=PhotoImage(file="slike_za_gui\rain.png").subsample(4)
            rain_prikaz=Label(root, image=rain,bg="#f3edea")
            rain_prikaz.place(x=350,y=190)
        elif vrijeme_ikona=="broken clouds" or vrijeme_ikona=="overcast clouds":
            clouds=PhotoImage(file="slike_za_gui\clouds.png").subsample(4)
            clouds_prikaz=Label(root, image=clouds,bg="#f3edea")
            clouds_prikaz.place(x=350,y=190)
        else:
            pass

        root.mainloop()
