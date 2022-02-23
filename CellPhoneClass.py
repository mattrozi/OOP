class CellPhone:
    def __init__(self, manu, model, price):
        self.__manufact = manu
        self.__model = model
        self.__retail_price = int(price)

    def set_manufact(self, manu):
        self.__manufact = manu

    def set_model(self, model):
        self.__model = model

    def set_retail_price(self, price):
        self.__retail_price = price

    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retail_price

    def __str__(self):
        return "The Model is: " + self.__model
