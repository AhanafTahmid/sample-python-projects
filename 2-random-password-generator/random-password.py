#Random password generator without oop
import random
def random_password(word="Ahnaf"):
    li = list(word)
    random.shuffle(li)
    return "Your new password is " + "".join(li)
print(random_password(input("Enter a word to generate a random password : \n")))

