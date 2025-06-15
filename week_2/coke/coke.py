def main():
    coin_tuple=(5,10,25)
    print(f"You only can use this coins '5', '10', '25'")
   
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

main()