month_list=[
    "January","February","March","April","May","June","July","August","September","October","November","December"
]
def main():
    while True:
        try:
            user_date=input(f"Date: ").title().strip()
            if user_date.count(" ")==2 and ("," in user_date):
                user_date=user_date.replace(",", "")
                x,y,z,=user_date.split()
                x=int(month_list.index(x)+1)
                y=int(y)
                z=int(z)
                if y>32:
                    raise EOFError
                elif x==2 and y>28:
                    raise EOFError
                elif x in (4,6,9,11) and y>30:
                    raise EOFError
                else:
                    break
            elif user_date.count("/")==2:
                x,y,z=user_date.split("/")
                x=int(x)
                y=int(y)
                z=int(z)
                if y>31 or x>12:
                    raise EOFError
                elif x==2 and y>28:
                    raise EOFError
                elif x in (4,6,9,11) and y>30:
                    raise EOFError
                else:
                    break
        except EOFError:
            pass
        except ValueError:
            pass
        except KeyError:
            pass
    print(f"{z}-{x:02}-{y:02}")

main()
