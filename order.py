class Order:

    def __init__(self,date,time):
        self.date = date
        self.time = time
        self.state='not accepted'

    def get_time(self):
        return self.time

    def get_date(self):
        return self.date

    def order_history_checking(self):
        pass

class OrderType:
    def __init__(self, tariff, comment,payment_method):
        self.tariff=tariff
        self.comment=comment
        self.payment_method=payment_method

    def choosing_tariff(self):
        pass

    def choosing_payment_method(self):
        pass

    def comment(self):
        pass

    def calculate_price(self):
        pass