#!/usr/bin/env python
"""Изменение формы слова"""
import sys


class WordMorph:
    allowed_words = ('товар',)

    def __init__(self, word='товар'):
        """Изменение формы слова с связи с числительным

        Args:
            word (str): слово. Должно присутствовать в списке релизованных
        """
        if word.lower() not in self.allowed_words:
            raise NotImplemented(f'Support of word "{word}" not implemented')

        self.word = word

    def get(self, num=0):
        """Получить форму слова в связке с переданным числительным

        Args:
            num (int): число для изменения формы слова

        Returns:
            str
        """
        if not isinstance(num, int) or num < 0:
            ValueError(f'num must be int and greater than zero'
                       f' and under {self.max_num}')

        # Последняя цифра
        last_digit = num % 10

        if (
                # Односоставные числительные
                (5 <= num <= 20)
                # Составные числительные
                or (last_digit == 0 or 5 <= last_digit <= 9)
        ):
            end = 'ов'
        elif last_digit == 1:
            end = ''
        elif 2 <= last_digit <= 4:
            end = 'а'
        else:
            ValueError(f'Incorrect value "{num}"')

        return f'{num} {self.word}{end}'


if __name__ == '__main__':
    default_num = 0

    try:
        num = int(input(f'Num ({default_num}): ') or default_num)
    except ValueError:
        print("Don't be stupid and enter valid number!", file=sys.stderr)
        exit(1)

    print(WordMorph('товар').get(num))
