
import requests

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

def main():
    while True:
        print("\n1. Get weather\n2. Get Wind Speed\n3. Get Pressure\n0. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            date = input("Enter the date (YYYY-MM-DD): ")
            temp = get_weather(date)
            if temp:
                print(f"The temperature on {date} is {temp} K")
            else:
                print("No data available for the given date.")

        elif choice == 2:
            date = input("Enter the date (YYYY-MM-DD): ")
            wind_speed = get_wind_speed(date)
            if wind_speed:
                print(f"The wind speed on {date} is {wind_speed} m/s")
            else:
                print("No data available for the given date.")

        elif choice == 3:
            date = input("Enter the date (YYYY-MM-DD): ")
            pressure = get_pressure(date)
            if pressure:
                print(f"The pressure on {date} is {pressure} hPa")
            else:
                print("No data available for the given date.")

        elif choice == 0:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try from above Numbers.")

if __name__ == "__main__":
    main()
