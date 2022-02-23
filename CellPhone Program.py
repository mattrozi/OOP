import CellPhoneClass as C


def main():

    Galaxy = C.CellPhone("Apple", "IPHONE 15", "500")
    print("The phone will be ", Galaxy.get_manufact())
    print(Galaxy.get_model())
    print("The original price is : ", Galaxy.get_retail_price())

    Galaxy.set_manufact("Galaxy")
    Galaxy.set_model("Samsung 8 ")
    Galaxy.set_retail_price("$100")

    print("The phone will be ", Galaxy.get_manufact())
    print(Galaxy.get_model())
    print(Galaxy.get_retail_price())

    print(Galaxy)


main()
