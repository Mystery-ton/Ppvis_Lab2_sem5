from viev import Viev
class Injector:
    def build(self):
        Viev().run()

if __name__ == "__main__":
    injector = Injector()
    injector.build()

