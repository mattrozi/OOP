import InsectClass as I


# The main function.
def main():
    my_insect = (
        I.Insect()
    )  # this creates an instance called 'my_coin' of the class 'Coin()'

    mosquito = I.Insect()
    housefly = I.Insect()

    mosquito.Length_of_flight()
    housefly.Length_of_flight()

    print("The Mosquito can fly ", mosquito.get_flight(), "miles")
    print("The housefly can fly ", housefly.get_flight(), "miles")


main()
