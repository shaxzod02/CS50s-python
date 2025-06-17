def main():
    grocery_dict=[]
    while True:
        try:
            user_input=input().upper().strip()
            if user_input=="":
                raise EOFError
            elif not user_input in grocery_dict:
                grocery_dict.update({user_input:1})
            else:
                grocery_dict[user_input]+=1
        except EOFError:
            break
    for item in sorted(grocery_dict):
        print(f"{grocery_dict[item]} {item}")

main()            