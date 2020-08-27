#Random Password generator with Python oop
import random
from tkinter import *
li = ""
class Random_Password:
    
    def __init__(self,word):
        self.word = word
        
        self.title = word.title("Random Password Generator")
        self.size = word.geometry("300x250")
        word.resizable(False,False)
        
        #First Label
        self.label = Label(text="Enter a word to generate \n a random password : ",font="Times 15")
        self.label.place(x=20,y=10)
        
        #Input Box
        self.entry = Entry(word,bg="gray80",font="Times 15")
        self.entry.insert("0","Password")
        self.entry.place(x=30,y=60)
        
        
        #Dynamically Label changing Label
        self.label2 = Label(word)
        self.label2.place(x=30,y=110)
        
        #Password Label
        self.label3 = Label(word,bg="tomato",text="")
        self.label3.place(x=111130)
        
        
        #Submit Button
        self.button = Button(word,text="Submit",cursor="hand2",command = self.submit)
        self.button.place(x=30,y=195)
    
        #Get the password button
        """ self.button = Button(word,text="Get the password",command = self.get_the_password)
        self.button.place(x=100,y=110) """  
        
    #Make Random Password
    def submit(self):
        self.button['text'] = ["Submitted"]
        submit = self.entry.get()
        self.entry.delete(0,END)
        submit_list = list(submit)
        try:
            random.choice(submit_list)
        except IndexError as e:
            print(e,"\nPlease Enter some words\n",end="")
        random.shuffle(submit_list)
        if len(submit_list)!=0:
            global li
            list_to_str = "".join(submit_list)
            li = list_to_str
            print("Your new password is ",list_to_str)
            self.label3.place(x=30,y=140)
            self.label2.configure(text="Your new password is \t\t",font="Times 12")
            self.label3.configure(text=li,font="Times 25")

            
    """ def get_the_password(self):
        submit = self.entry.get()
        submit_list = list(submit)
        randoms = random.choice(submit_list)
        random.shuffle(submit_list)
        list_to_str = "".join(submit_list)
        while list_to_str!=submit:
            print(submit) """
            
    
def random_password():
    root = Tk()
    #root.title("hello")
    app = Random_Password(root)
    root.mainloop()

if __name__ == "__main__":
    random_password()