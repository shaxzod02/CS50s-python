mexico={
    " Taco": 4.25,
    "Burrito": 7.50,
    "Nachos": 11.00,
    "Quesadilla":8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total=0
    key_value=0
    while key_value!=-1:
        key_value=get_order()
        if key_value in mexico:
            print(f"${sum_up(total,key_value)}")

def get_order():
    while True:
        try:
            order=input(f"Item: ").strip().lower()
            order=order.title()
            return mexico.get(order)
        except EOFError:
            pass

def sum_up(total, key_value):
    return total+key_value