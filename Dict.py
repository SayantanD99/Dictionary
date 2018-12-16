import json
from difflib import get_close_matches
data = json.load(open("dict_data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("\n Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "\n The word doesn't exist. Please double check it."
        else:
            return "\n We didn't understand your entry."
    else:
        return "\n The word doesn't exist. Please double check it."
ch=1
try :
    while ch==1:
        word = input("\n\n Enter word: ")
        output = translate(word)
        if type(output) == list:
            for item in output:
                print("\n", item)
            ch = int(input("\n \n Enter 1 to Continue the process and 0 to exit : "))
            if ch==1 :
               continue
            elif ch==0 :
                exit("\n Thank You...")
            else :
                print("\n Wrong Input...NOT ACCEPTED")
                exit("\n \n Try to read the Instructions Carefully :)")
        else:
         print("\n",output)
         ch = int(input("Enter 1 to Continue the process and 0 to exit : "))
         if ch == 1:
             continue
         elif ch == 0:
             exit("\n \n Thank You...")
         else:
             print("\n Wrong Input...NOT ACCEPTED")
             exit("\n \n Try to read the Instructions Carefully :)")

except ValueError :
    print("\n \n Wrong Input...NOT ACCEPTED")
    exit("\n Try to read the Instructions Carefully :)")