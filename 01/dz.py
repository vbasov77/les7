"""
Задание 1.
Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).
В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time
Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

import os
from time import sleep
from turtle import clear


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self, color):
        self.__color = color
        print(color)


while True:
    os.system('cls||clear')
    red = TrafficLight('Красный')
    red.running('Красный')
    sleep(7)

    os.system('cls||clear')
    yell = TrafficLight('Жёлтый')
    yell.running('Жёлтый')
    sleep(2)

    os.system('cls||clear')
    green = TrafficLight('Зелёный')
    green.running('Зелёный')
    sleep(7) 
