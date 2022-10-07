import datetime

class Calculator:
    def __init__(self, limit):
        self.limit=limit
        self.records = []
    def add_record(self, record):
        self.records.append(record)
    def get_today_start(self):
        today_date=datetime.date.today()
        today_sum=sum(record.amount for record in self.records
                      if record.date==today_date)
        return today_sum
    def get_week_start(self):
        today_date = datetime.date.today()
        ago=today_date-datetime.timedelta(7)
        week_sum=sum(record.amount for record in self.records
                      if ago<=record.date<=today_date)
        return week_sum
    def remained(self):
        return self.limit-self.get_today_start()
class Record:
    def __init__(self, amount, comment, date=None):
        self.amount=amount
        self.comment=comment
        if date is not None:
            self.date = datetime.datetime.strptime(date, '%d.%m.%Y').date()
        else:
            self.date = datetime.date.today()

class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        calories_remained=self.remained()
        if calories_remained<=0:
            return "Stop eating"
        return f"Today you can eat something else, but with a total calorie content of no more then {calories_remained} Kcal"

class CashCalculator(Calculator):
    USD_R=58.0
    EURO_R=56.0
    RUB_R=1.0
    def get_today_cash_remained(self, currency):
        cash_remained = self.remained()
        currencies={
            "EURO": ("euro", self.EURO_R),
            "USD": ("usd", self.USD_R),
            "RUB": ("rub", self.RUB_R),
            }
        cur, rate=currencies.get(currency)
        cash_remained=round(cash_remained/rate, 2)
        if cash_remained==0:
            return "No money, but you hold on"
        if currency not in currencies:
            return "Rate not found"
        if cash_remained>0:
            return f"Left for today {cash_remained} {cur}"
        cash_remained=abs(cash_remained)
        return f"No money, but you hold on. Your duty:  {cash_remained} {cur}"
# cash_calculator=CashCalculator(1300)
# cash_calculator.add_record(Record(amount=1186,comment='Кусок тортика. И ещё один.'))
# cash_calculator.add_record(Record(amount=145, comment='кофе'))
# cash_calculator.add_record(Record(amount=300, comment='Серёге за обед'))
# cash_calculator.add_record(Record(amount=3000, comment='бар в Танин др'))
# cash_calculator.add_record(Record(amount=145, comment='Безудержный шопинг', date='08.03.2019'))
# cash_calculator.add_record(Record(amount=1568,comment='Наполнение потребительской корзины',date='09.03.2019'))
# cash_calculator.add_record(Record(amount=691, comment='Катание на такси', date='08.03.2019'))
# print(cash_calculator.get_today_cash_remained('RUB'))

calories_calculator=CaloriesCalculator(1000)
calories_calculator.add_record(Record(amount=1186,comment='Кусок тортика. И ещё один.',date='24.02.2019'))
calories_calculator.add_record(Record(amount=145, comment='кофе'))
calories_calculator.add_record(Record(amount=300, comment='Серёге за обед'))
calories_calculator.add_record(Record(amount=3000, comment='бар в Танин др'))
print(calories_calculator.get_calories_remained())


# class TestStat(unittest.TestCase, Calculator):
#     def test_calc(self):
#         self.assertTrue(self.__init__(self.limit) > 0, "Количество не может быть отрицательным")
    
# if __name__ == '__main__':
#     unittest.main()

# def test_no_root():
#    res = CaloriesCalculator.get_calories_remained()
#    assert len(res) == 0