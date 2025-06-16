def main():
    coin_tuple=(5,10,25)
    print(printable_machine (coin_tuple))
   
    amount_due=50
    while amount_due > 0:
        print(f"Amount due: {amount_due}")
        coin=input(f"Insert Coin: ")
        while coin.isnumeric()!=True:
            print("you only can use the coins above.")
            coin=input(f"Insert Coin: ")
        if int(coin) in coin_tuple:
            amount_due=amount_due-int(coin)
        else:
            continue
    print(f"change owed: {str(amount_due).strip("-")}")

def printable_machine(coins):
    return f"""
    You only can use this coins {coins[0]}, {coins[1]}, {coins[2]}
    """

main()