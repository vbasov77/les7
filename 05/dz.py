"""
Задание 5.
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем публичный атрибут title (название) и публичный метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса: Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return print('Запуск отрисовки.')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self, title):
        self.title = title
        print(f'В классе Pen переопределен метотод с заголовком {title}')


class Pencil (Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self, title):
        self.title = title
        print(f'В классе Pencil переопределен метотод с заголовком {title}')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self, title):
        self.title = title
        print(f'В классе Handle переопределен метотод с заголовком {title}')


stationery = Stationery('Канцелярская принадлежность')
print(stationery.draw())

input()

pen = Pen('Ручка')
print(pen.draw('Ручка'))

input()

pencil = Pencil('Карандаш')
print(pencil.draw('Карандаш'))

input()

handle = Handle('Маркер')
print(handle.draw('Маркер'))
