from passanger import Passanger
from driver import Driver
from order import Order
#from viev import Viev

class System:

    def __init__(self):
        pass

    def user_entering(self, login:str,password:str):
        pass

    def passanger_registration(self,data:list[str]):
        pass

    def driver_registration(self,data:list[str]):
        pass

    def get_data(self,user):
        return list[str]

    def grade(self,whoGets:Driver,whoPuts:Passanger):
        pass

    def leave_feedback(self,whoGets,whoPuts):
        pass

    def send_massage(self,text:str,whoGets,whoPuts):
        pass

    def get_order_histiry(self,user):
        return list[Order]

    def show_balance(self,driver:Driver):
        return int

    def checkout(self,passanger:Passanger,driver:Driver):
        return Order

    def change_passanger_data(self,data:list[str],passanger:Passanger):
        pass

    def change_driver_data(self,data:list[str],driver:Driver):
        pass