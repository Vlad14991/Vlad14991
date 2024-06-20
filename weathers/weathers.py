import tkinter as tk
import requests


def get_weather():
    city = "Красноярск"
    api_key = "b60ebeac37acb4ad68f7796548ded19c"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        root.title('Погода в городе Красноярск')
        label_temp.config(text='Температура: ' + str(round(data['main']['temp'])) + '°C')
        label_feels_like.config(text='Ощущаемая температура: ' + str(round(data['main']['feels_like'])) + '°C')
        label_humidity.config(text='Влажность: ' + str(data['main']['humidity']) + '%')
        label_wind_speed.config(text='Ветер: ' + str(round(data['wind']['speed'])) + ' м/с')
    else:
        root.title('Произошла ошибка: ' + str(response.status_code))


root = tk.Tk()
root.geometry('300x200')

label_temp = tk.Label(root, text='Температура: ')
label_temp.pack(pady=5)

label_feels_like = tk.Label(root, text='Ощущаемая температура: ')
label_feels_like.pack(pady=5)

label_humidity = tk.Label(root, text='Влажность: ')
label_humidity.pack(pady=5)

label_wind_speed = tk.Label(root, text='Ветер: ')
label_wind_speed.pack(pady=5)

root.after(2000, get_weather)

root.mainloop()
