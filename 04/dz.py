

import os
from time import sleep


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = is_police

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Скорость {self.speed}')


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, speed):
        self.speed = speed
        if speed > 60:
            return print('Вы привысили скорость!')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, speed):
        self.speed = speed
        if speed > 40:
            return print('Вы привысили скорость!!!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)



os.system('cls||clear')
car = Car(100, 'Белый', 'Ваз', 'да')
print(
    f'Скорость {car.speed}, Цвет: {car.color}, Название: {car.name}, Is_police: {car.is_polise}')
car.go()
car.stop()
car.turn('налево')

sleep(5)

os.system('cls||clear')
town_car = TownCar(90, 'Синий', 'Хонда', 'да')
print(f'Скорость {town_car.speed}, Цвет: {town_car.color}, Название: {town_car.name}, Is_police: {town_car.is_polise}')
town_car.go()
town_car.stop()
town_car.turn('направо')
town_car.show_speed(town_car.speed)

sleep(5)
os.system('cls||clear')
work_car = WorkCar(200, 'Чёрный', 'БМВ', False)
print(f'Скорость {work_car.speed}, Цвет: {work_car.color}, Название: {work_car.name}, Is_police: {work_car.is_polise}')
work_car.go()
work_car.stop()
work_car.turn('направо')
work_car.show_speed(work_car.speed)
