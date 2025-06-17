def main():
    x,y=get_fraction(f"Fraction: ")
    print(f"{fraction_to_porcentage(x,y):.0f}%")

def get_fraction(prompt):
    fraction=input(prompt).strip()
    fraction=fraction.replace(" ", "")
    try:
        if not (fraction.count("/")==1):
            raise ValueError
        elif not ((fraction.replace("/", "")).isdigit()):
            raise ValueError
        elif fraction[fraction.index("/")+1:len(fraction)]=="0":
            raise ZeroDivisionError
        elif int(fraction[:fraction.index("/")])> int(fraction[fraction.index("/")+1:len(fraction)]):
            raise ZeroDivisionError
        return fraction.split("/")
    except ZeroDivisionError:
        pass
    except ValueError:
        pass


def fraction_to_porcentage(x,y):
    if (int(x)/int(y) * 100)==100:
        return "F"
    elif (int(x)/int(y) * 100)==0:
        return "E"
    return f"{int(x)/int(y) * 100:.0f}%"

main()