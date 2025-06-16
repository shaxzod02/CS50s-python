def main():
    plate= input(f"input: ")
    if is_valid(plate):
        print(f"Valid")
    else:
        print("Invalid")    

def is_valid(plate):
    if plate.count(" ")>0:
        return False
    elif (1<len(plate)<7)==False:
        return False
    elif str(plate[0:2]).isalpha()==False:
        return False
    elif str(plate).isalnum()==False:
        return False
    else:
        p=0
        while p < len(plate):
            if str(plate[p]).isdigit():
                return str(plate[p:len(plate)]).isdigit()
            else:
                p+1
        return True

def word_letters_converter(word):
    word=word.replace("", " ")
    letters=word.split()
    return letters
main()            
     