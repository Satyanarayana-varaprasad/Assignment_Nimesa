import requests
import tkinter as tk
from tkinter import *
from tkinter import messagebox

API_KEY = "b6907d289e10d714a6e88b30761fae22"
BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly"

def get_weather(date):
    url = f"{BASE_URL}?q=London,us&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    for forecast in data["list"]:
        if forecast["dt_txt"].split()[0] == date:
            return forecast["main"]["temp"]
    return None

def get_wind_speed(date):
    url = f"{BASE_URL}?q=London,us&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    for forecast in data["list"]:
        if forecast["dt_txt"].split()[0] == date:
            return forecast["wind"]["speed"]
    return None

def get_pressure(date):
    url = f"{BASE_URL}?q=London,us&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    for forecast in data["list"]:
        if forecast["dt_txt"].split()[0] == date:
            return forecast["main"]["pressure"]
    return None

def show_weather():
    date = date_entry.get()
    if not date:
        messagebox.showwarning("Warning", "Please enter a date.")
        return

    choice = choice_var.get()
    if choice == 1:
        result = get_weather(date)
        if result:
            result_label.config(text=f"The temperature on {date} is {result}°C")
        else:
            result_label.config(text="No data available for the given date.")
    elif choice == 2:
        result = get_wind_speed(date)
        if result:
            result_label.config(text=f"The wind speed on {date} is {result} m/s")
        else:
            result_label.config(text="No data available for the given date.")
    elif choice == 3:
        result = get_pressure(date)
        if result:
            result_label.config(text=f"The pressure on {date} is {result} hPa")
        else:
            result_label.config(text="No data available for the given date.")
    else:
        messagebox.showwarning("Warning", "Invalid choice. Please try again.")

# GUI setup
root = tk.Tk()
root.title("Weather Forecast App")

T=Label(root,text='Weather Forecast App', height=2,width=35,font=14)
T.pack()

choice_var = tk.IntVar()

date_label = tk.Label(root, text="Enter the date (YYYY-MM-DD):", height=2,width=35)
date_label.pack()
date_entry = tk.Entry(root)
date_entry.pack()

radio_frame = tk.Frame(root)
radio_frame.pack()

tk.Radiobutton(radio_frame, text="Get weather", variable=choice_var, value=1).grid(row=0, column=0, padx=5, pady=5)
tk.Radiobutton(radio_frame, text="Get Wind Speed", variable=choice_var, value=2).grid(row=0, column=1, padx=5, pady=5)
tk.Radiobutton(radio_frame, text="Get Pressure", variable=choice_var, value=3).grid(row=0, column=2, padx=5, pady=5)

submit_button = tk.Button(root, text="Submit", command=show_weather)
submit_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
