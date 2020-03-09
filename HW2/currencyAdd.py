from pycbrf.toolbox import ExchangeRates
from datetime import datetime


class CurrencyAdder:
    def __init__(self, curr, name='RUB'):
        self.value = curr
        self.name = name
        if name != 'RUB':
            self.rub = self._to_local_current()
        else:
            self.rub = curr

    def __repr__(self):
        return '{value: ' + str(self.value) + ', name: ' + str(self.name) + ', rub: ' + str(self.rub) + '}'

    def __str__(self):
        return 'Currency (value= ' + str(self.value) + ', age= ' + self.name + ', rub= ' + str(self.rub) + ')'

    def __add__(self, other):
        try:
            if self.name == other.name:
                return self.value + other.curr
            else:
                rates = self._get_currency()
                if self.name != 'RUB':
                    try:
                        curr1 = rates[other.name].value
                    except KeyError as e:
                        raise ValueError('Undefined unit: {}'.format(e.args[0]))
                else:
                    curr1 = 1
                return round(float((self.rub + other.rub)/curr1), 2)
        except AttributeError:
            return self.value + other

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

    def _to_local_current(self):
        rates = self._get_currency()
        try:
            cur = rates[self.name].value
        except KeyError as e:
            raise ValueError('Undefined unit: {}'.format(e.args[0]))
        return round(float(self.value * cur), 2)
