import datetime

class Calculator:
    def __init__(self, limit):
        self.limit=limit
        self.records = []
    def add_record(self):
        self.records.append(Record)
    def get_today_start(self):
        today_date=datetime.date.today()
        today_sum=sum(Record.amount for record in self.records
                      if record.date==datetime.today)
    def get_week_start(self):
        today_date = datetime.date.today()
        ago=today_date-datetime.timedelta(7)
        week_sum=sum(Record.amount for record in self.records
                      if ago<=record.date<=today_date)
        return week_sum
    def remained(self):
        return self.limit-self.get_today_start()
class Record:
    def __init__(self, amount, comment, date):
        self.amount=amount
        self.comment=comment
        if None==date:
            datetime.date.today()
        else:
            datetime.datetime.date()

class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        calories_remained=self.remained()
        if calories_remained<=0:
            return "Stop eating"
        return "Today you can eat something else, but with a total calorie content of no more then " + calories_remained + " Kcal"

class CashCalculator(Calculator):
    USD=58
    EURO=56
    RUB=1.0
    def get_today_cash_remained(self, currency):
        cash_remained = self.remained()

        currencies={"EURO": ("EURO", self.EURO_RATE),
                    "USD": ("USD", self.USD_RATE),
                    "RUB": ("RUB", self.RUB_RATE)}
        if currency is not currencies:
            return "Rate not found"
        rate=currencies.get(currency)
        cash_remained=round(cash_remained/rate, 2)
        if cash_remained==0:
            return "No money, but you hold on"
        if cash_remained>0:
            return "Left for today "+cash_remained
        if cash_remained<0:
            cash_remained=abs(cash_remained)
            return "No money, but you hold on. Your duty: " + cash_remained

