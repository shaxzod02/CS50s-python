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
    while key_value!=mexico[""]:
        key_value=get_order()
        if key_value!=mexico[""]:
            total+=key_value
            print(f"Total: ${total}")
        

def get_order():
    while True:
        
            order=input(f"Item: ").strip().lower()
            order=order.title()
            try:
               return mexico[f"{order}"]
            except:
                EOFError
                

def sum_up(total, key_value):
    return total+key_value

main()