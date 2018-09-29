#!/usr/bin/env python
"""Создание матрицы"""
import sys


class Matrix:
    def __init__(self, rows=3, cells=4, value=5):
        """Создает матрицу указанной размерности

        Матрица размером rows x cells заполняется значениями value.

        Args:
            rows (int): количество строк
            cells (int): значений в строке
            value: значение для заполнения
        """
        if not isinstance(rows, int) or not isinstance(cells, int) \
                or rows <= 0 or cells <= 0:
            raise ValueError('rows, cells must be positive int numbers')

        self.matrix = []

        for i in range(rows):
            self.matrix.append([])

            for j in range(cells):
                self.matrix[i].append(value)

    def __getitem__(self, item):
        return self.matrix[item]

    def __setitem__(self, key, value):
        self.matrix[key] = value

    def __str__(self):
        return '[' + '\n '.join(str(row) for row in self.matrix) + ']'


if __name__ == '__main__':
    default_n = 3
    default_m = 4
    default_d = 5

    try:
        n = int(input(f'N ({default_n}): ') or default_n)
        m = int(input(f'M ({default_m}): ') or default_m)
        d = float(input(f'D ({default_d}): ') or default_d)
    except ValueError:
        print("Don't be stupid and enter valid number!", file=sys.stderr)
        exit(1)

    print(Matrix(n, m, d))
