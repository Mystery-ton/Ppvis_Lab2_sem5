class Driver:

    def __init__(self, login, password, email,tlfNum, name,city,expereance,car,carNum):
        self.login = login
        self.password = password
        self.email = email
        self.tlfNum = tlfNum
        self.name = name
        self.rating = None
        self.city = city
        self.expereance = expereance
        self.car=car
        self.carNum=carNum
        self.balance=None

    def calculateRating(self):
        pass

    def get_login(self):
        return self.login

    def get_password(self):
        return self.password

    def get_email(self):
        return self.email

    def get_name(self):
        return self.name

    def get_tlfNum(self):
        return self.tlfNum

    def get_rating(self):
        return self.rating

    def get_balance(self):
        return self.bank

    def set_balance(self,balance):
        self.balance=balance

    def recive_order(self):
        pass

    def change_data(self):
        pass