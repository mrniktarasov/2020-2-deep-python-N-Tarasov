from pycbrf.toolbox import ExchangeRates
from datetime import datetime


class CurrencyAdder:
    def __init__(self, curr, name=''):
        self.value = curr
        self.name = name

    def __repr__(self):
        return 'CurrencyAdder: {value: ' + str(self.value) + ', name: ' + str(self.name) + '}'

    def __str__(self):
        return '' + str(self.value) + ' ' + self.name

    def __add__(self, other):
        try:
            if self.name == other.name:
                return CurrencyAdder(self.value + other.value, self.name)
            else:
                rates = self._get_currency()
                if self.name != 'RUB' and self.name != '':
                    try:
                        curr1 = rates[self.name].value
                    except KeyError as e:
                        raise ValueError('Undefined unit: {}'.format(e.args[0]))
                else:
                    curr1 = 1
                if other.name != '':
                    try:
                        curr2 = rates[other.name].value
                    except KeyError as e:
                        raise ValueError('Undefined unit: {}'.format(e.args[0]))
                else:
                    curr2 = 1
                if self.name != '' and other.name != '':
                    cur = round(float((self.value * curr1 + other.value * curr2)/curr1), 2)
                    return CurrencyAdder(cur, self.name)
                elif self.name == '':
                    cur = round(float((self.value + other.value)), 2)
                    return CurrencyAdder(cur, other.name)
                else:
                    cur = round(float((self.value + other.value)), 2)
                    return CurrencyAdder(cur, self.name)
        except AttributeError:
            return CurrencyAdder(self.value + other, self.name)

    def _get_currency(self):
        rates = ExchangeRates(datetime.now())
        return {
            'USD': rates['USD'],
            'EUR': rates['EUR'],
            'GBP': rates['GBP'],
            'JPY': rates['JPY'],
            'CHF': rates['CHF'],
            'CNY': rates['CNY'],
        }
