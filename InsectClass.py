import random


class Insect:
    # The _ _init_ _ method initializes the
    def __init__(self):
        self.wings = 2
        self.legs = 4
        self.flight = 0

    def Length_of_flight(self):
        self.flight = random.randint(1, 10)

    def get_flight(self):
        return self.flight
