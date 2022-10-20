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
        self._length = float(length)
        self._width = float(width)

    def get_asphalt_masses(self, thickness):
        try:
            return (self._length * self._width * thickness * self._thickness_canvas)
        except TypeError:
            return None



length = float(input('Введите длинну: '))
width = float(input('Введите ширину: '))
obj = Road(length, width)
result = obj.get_asphalt_masses(25)

print(f'Масса дорожного покрытия составит: {result} кг = {result / 1000} тонн')

