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


from time import sleep


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки.'


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

sleep(2)

pen = Pen('Ручка')
pen.draw('Ручка')

sleep(2)

pencil = Pencil('Карандаш')
pencil.draw('Карандаш')

sleep(2)

handle = Handle('Маркер')
handle.draw('Маркер')
