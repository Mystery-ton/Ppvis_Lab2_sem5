from kivy.config import Config
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from Screens import *

Config.set('graphics', 'resizable', '0')

Builder.load_file("D:/PPVIS-2/PPVIS-2/my.kv")


class Viev(App):
    Window.clearcolor = (.60,.70,.90,1)
    def build(self):
        self.title="Main Window"
        Window.size = (450, 600)
        sm = ScreenManager()
        sm.add_widget(Reg_or_log(name='registration_or_login'))
        sm.add_widget(Start(name='start'))
        sm.add_widget(Login(name='login'))
        sm.add_widget(Reg_driver(name='registration_driver'))
        sm.add_widget(Reg_passanger(name='registration_passanger'))
        sm.add_widget(Driver_menu(name='driver_menu'))
        sm.add_widget(Passanger_menu(name='passanger_menu'))
        sm.add_widget(Change_driver_data(name='change_driver_data'))
        sm.add_widget(Change_passanger_data(name='change_passanger_data'))
        sm.add_widget(Show_rating(name='show_rating'))
        sm.add_widget(Show_reviewes(name='show_reviewes'))
        sm.add_widget(Show_order_history(name='show_order_history'))
        sm.add_widget(Show_balance(name='show_driver_balance'))
        sm.add_widget(Looking_for_car(name='looking_for_car'))
        sm.add_widget(Get_order(name='get_Order'))
        sm.add_widget(Make_order(name='make_order'))
        return sm

        


