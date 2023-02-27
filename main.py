from tkinter import *
import requests
from tkinter import messagebox


API_KEY = "Your Api Key"
URL = "https://api.openweathermap.org/data/2.5/weather"


def get_data():
    params = {
        "q": city_entry.get(),
        "appid":API_KEY
    }

    response = requests.get(URL, params=params)
    response.raise_for_status()

    data = response.json()
    weather = data['weather'][0]['main']
    desc = data['weather'][0]['description']
    temp = data['main']['temp']

    if len(city_entry.get()) == 0:
        messagebox.showwarning(title="Failed", message="You have to ensure that any field was empty")
    else:
        messagebox.showinfo(title=f"{city_entry.get()}", message=f"Weather: {weather}\n"
                                                           f"description: {desc}\n"
                                                           f"temperature: {temp}")


window = Tk()
window.title("Weather")
window.config(padx=50, pady=50)

#label
label = Label(text="Enter city name", font=("Arial", 20, "bold"))
label.grid(column=1, row=0, columnspan=2, pady=20)

#Entry
city_entry = Entry(width=40)
city_entry.grid(column=1, row=1, columnspan=2)

#Button
check_button = Button(text="Check Wheater", font=("Arial", 15, "normal"), command=get_data)
check_button.grid(column=1, row=2, columnspan=2, pady=20)

window.mainloop()