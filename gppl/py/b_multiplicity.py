#!/usr/bin/env python
"""Кратные числа"""
import sys


class Multiplicity:
    def __init__(self, min=0, max=100, multiplicity=10):
        """Получение кратных чисел в диапазоне

        Выводит числа, кратные заданному, в диапазоне [min:max]

        Args:
            min (int): минимальное значение
            max (int): максимальное значение
            multiplicity (int): кратность

        Returns:
            int

        Examples:
            >>> next(Multiplicity(13, 30, 10))
            20
        """
        if min > max:
            raise ValueError('min must be less or equal max')
        
        self.min = min
        self.max = max
        self.multiplicity = multiplicity
        self.next_value = None
        
    def __iter__(self):
        return self

    def __next__(self):
        min_value = self.next_value or self.min - 1  # Включаем минимальное значение

        # Определяем необходимый прирост
        self.next_value = (min_value + self.multiplicity
                           - (min_value % self.multiplicity))

        if self.next_value > self.max:
            raise StopIteration

        return self.next_value
            

if __name__ == '__main__':
    default_min = 45
    default_max = 670
    default_mp = 10
    
    try:
        mn = int(input(f'Min ({default_min}): ') or default_min)
        mx = int(input(f'Max ({default_max}): ') or default_max)
        mp = int(input(f'Multiplicity ({default_mp}): ') or default_mp)
    except ValueError:
        print("Don't be stupid and enter valid numbers!", file=sys.stderr)
        exit(1)

    for m in Multiplicity(mn, mx, mp):
        print(m)
