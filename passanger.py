class Passanger:

    def __init__(self,login,password,email,tlfNum,name,bank):
        self.login = login
        self.password = password
        self.email = email
        self.tlfNum = tlfNum
        self.name = name
        self.rating = None
        self.bank = bank
        self.reviewList = list[str]

    def checkout(self, team):
        pass

    def chooseCheckoutType(self):
        pass

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

    def get_bank(self):
        return self.bank

    def change_data(self):
        pass