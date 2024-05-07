import requests
from threading import Timer
import sqlite3
import datetime
import xl


def db_create(): # Создание базы данных
    connection = sqlite3.connect("my_database.db")
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS weather (
    temp, 
    wind_speed, 
    wind_dir, 
    pressure, 
    precipitation, 
    date
    )
    ''')
    connection.commit()
    connection.close()


def repeater(interval, function): #Таймер
    Timer(interval, repeater, [interval, function]).start()
    function()


def weather(): #Запрос к API
    access_key = '92633492-fa21-4cb4-9b9f-504feffab676'

    headers = {
        'X-Yandex-Weather-Key': access_key
    }

    response = requests.get('https://api.weather.yandex.ru/v2/forecast?lat=55.42&lon=37.22', headers=headers)

    connect = sqlite3.connect("my_database.db")
    cur = connect.cursor()

    cur.execute('INSERT INTO weather '
                '(temp, wind_speed, wind_dir, pressure, precipitation, date) VALUES (?, ?, ?, ?, ?, ?)',
                (response.json()['fact']['temp'], response.json()['fact']['wind_speed'],
                 response.json()['fact']['wind_dir'], response.json()['fact']['pressure_mm'],
                 response.json()['fact']['condition'], datetime.datetime.now()))
    connect.commit()
    connect.close()


db_create()
repeater(180, weather)
xls = input('Запрос данных в excel(+)')
if xls == '+':
    xl.xl()
