#!/usr/bin/env python
"""Сортировка людей"""


class Meat:
    def __init__(self, name, age):
        """Данные людей

        Args:
            name (str): Имя
            age (int): Возраст
        """
        if not isinstance(name, str) or len == 0:
            raise ValueError('name must be non-empty str')

        if not isinstance(age, int) or age < 0:
            raise ValueError('age must be non-negative int')

        self.name = name
        self.age = age

    def __repr__(self):
        return f'<{self.name}, {self.age}>'


class MeatSorter:
    def __init__(self):
        """Контейнер для хранения и сортировки личностей"""
        self.storage = []

    def __iadd__(self, other):
        self.storage.append(other)
        return self

    def __str__(self):
        return '[' + '\n '.join(map(str, self.storage)) + ']'

    def by_name(self, desc=False):
        """Сортировка по имени

        Args:
            desc (bool): в убывающем порядке

        Returns:
            list
        """
        return sorted(self.storage, key=lambda i: i.name, reverse=desc)

    def by_age(self, desc=True):
        """Сортировка по возрасту

        Args:
            desc (bool): в убывающем порядке

        Returns:
            list
        """
        return sorted(self.storage, key=lambda i: i.age, reverse=desc)


if __name__ == '__main__':
    import random

    # Случайный возраст
    rnd = lambda: random.randint(0, 100)

    storage = MeatSorter()

    # Наполняем псевдолюдьми
    storage += Meat('Jonelle Lytch', rnd())
    storage += Meat('Glenda Cabana', rnd())
    storage += Meat('Alene Coomer', rnd())
    storage += Meat('Isidro Trexler', rnd())
    storage += Meat('Palmer Saffold', rnd())
    storage += Meat('Lynne Mayse', rnd())
    storage += Meat('Sandee Callihan', rnd())
    storage += Meat('Theron Stroup', rnd())
    storage += Meat('Tracy Criger', rnd())
    storage += Meat('Ardath Chacko', rnd())

    print(storage)
    print('By name:', storage.by_name())
    print('By age:', storage.by_age())