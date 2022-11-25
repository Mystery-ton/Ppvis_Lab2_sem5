from kivy.uix.screenmanager import Screen
from system import System
from passanger import Passanger
from tripResults import TripResults
from orderHistipy import OrderHistory
from order import Order


class Reg_or_log(Screen):
    def checkbox_click(self, instance, value):
        if value is True:
            print("Checkbox Checked")
        else:
            print("Checkbox Unchecked")
    pass

class Change_driver_data(Screen):
    __order: Order

    pass

class Login(Screen):

    def ask_login(self):
        pass

    def ask_password(self):
        pass

class Start(Screen):
    def checkbox_click(self, instance, value):
        if value is True:
            print("Checkbox Checked")
        else:
            print("Checkbox Unchecked")

class Change_passanger_data(Screen):
    pass

class Reg_driver(Screen):
    def ask_login(self):
        pass

    def ask_password(self):
        pass

    def ask_personal_data(self):
        pass

class Reg_passanger(Screen):
    def ask_login(self):
        pass

    def ask_password(self):
        pass

    def ask_personal_data(self):
        pass

class Make_order(Screen):
    pass

class Get_order(Screen):
    pass

class Show_rating(Screen):
    pass

class Show_reviewes(Screen):
    pass

class Show_order_history(Screen):
    pass

class Show_balance(Screen):
    pass

class Driver_menu(Screen):
    pass

class Passanger_menu(Screen):
    pass
class Looking_for_car(Screen):
    pass