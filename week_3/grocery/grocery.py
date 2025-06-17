def main():
    grocery_list=[]
    while True:
        try:
            user_input=input().upper()
            if user_input=="":
                raise EOFError
            elif not user_input in grocery_list:
                grocery_list.append(user_input)
            else:
                continue
        except EOFError:
            break
    grocery_list=sorted(grocery_list)
    for i in range(len(grocery_list)):
        print(f"{i+1} {grocery_list[i]}")

main()            