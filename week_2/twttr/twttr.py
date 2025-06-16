def main():
    user_input=input(f"input: ")
    print(f"output: {shortten_converter(user_input)} ")
def shortten_converter(word):
    vowels=("a", "e", "i", "o", "u")
    word=word.replace("", " ")
    letters=word.split()
    p=0
    while p<len(letters):
        if str (letters[p]).lower in vowels:
            letters[p]=""
            p+=1
        else:
            p+=1
    return "".join(letters)            

main()