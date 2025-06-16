camel_case=input(f"camelCase: ").strip()
print("snake_case: ", end="")

for letter in camel_case:
    if letter.isupper():
        print("_"+letter.lower(), end="")
    else:
        print(letter, end="")    