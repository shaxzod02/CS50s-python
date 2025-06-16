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

main() 
#another version with for-in loop

def main_2():
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
    elif plate.isalpha():
        return True
    else:
        space=" "
        z=""
        for char in plate:
            if str(char).isdigit():
                z=z+"1"
        return not (space in z.strip())

main_2() 

