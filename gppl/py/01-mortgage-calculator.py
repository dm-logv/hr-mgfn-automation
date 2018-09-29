#!/usr/bin/env python
"""Ипотечный калькулятор"""


class MortgageCalculator:
    def __init__(self, value=1_000_000, rate=0.1, term=10):
        """Калькулятор расчета переплат по ипотеке
        
        Args:
            value (int): размер кредита
            rate (float): процентная ставка
            term (int): количество лет

        Raises:
            ValueError: неадекватные значения или типы данных
        """
        for k, v in (('value', value), ('rate', rate), ('term', term)):
            if not isinstance(v, (int, float)) or v <= 0:
                raise ValueError(f'{k} must be int or float '
                                 f'and must be greather than zero')
            
        self.value = value
        self.rate = rate
        self.term = term

    @property
    def overpayments(self):
        """Расчет суммарной переплаты

        Returns:
            float
        """
        return self.value * self.rate * self.term


if __name__ == '__main__':
    # Значения по умолчанию
    default_value = 2_000_000
    default_rate = 0.1
    default_term = 5

    # Ввод знаяений от пользователя
    # При пустых значениях используем значения по умолчанию
    try:
        S = float(input(f'Credit value ({default_value}): ') or default_value)
        p = float(input(f'Rate as decimal fraction ({default_rate}): ')
                  or default_rate)
        years = float(input(f'Term ({default_term}): ') or default_term)
    except ValueError:
        print("Don't be stupid and enter valid numbers!")
        exit(1)

    perepl = MortgageCalculator(S, p, years).overpayments
    print('Total overpayments:', perepl)

