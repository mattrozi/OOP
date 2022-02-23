import CoinClass as C


def show_coin_status(coin_obj):
    print("This side is up", coin_obj.get_sideup())


def flip(coin_obj):
    coin_obj.toss()


my_coin = C.Coin()
flip(my_coin)
show_coin_status(my_coin)
