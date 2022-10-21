"""
Задание 2.
Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.
Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""



class Road:
    _thickness_canvas = 0.05

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_asphalt_masses(self, thickness):
        try:
            return (self._length * self._width * thickness * self._thickness_canvas)
        except TypeError:
            return None



length = int(input('Введите длинну: '))
width = int(input('Введите ширину: '))
obj = Road(length, width)
result = int(obj.get_asphalt_masses(25))

print(f'Масса составит: {result} кг = {int(result / 1000)} тонн')

