#Currency converter with oop
from tkinter import *
from tkinter.font import Font
class Currency_Converter(object):
    def __init__(self,master):
        self.master = master
        
        #Window of the Application
        master.title("Hello")
        master.geometry("300x300")
        
        try:
            master.iconphoto(False, PhotoImage(file='I:\Web and Programming\Month\\2020\\2.June\\15.Currency converter(27)\icon.png'))
        except TclError:
            print("Could not open the image")
        #master.call('wm', 'iconphoto', master._w, PhotoImage(file='I:\Web and Programming\Month\\2020\\2.June\\15.Currency converter\icon.png'))
	    
  
        fonts =Font(weight="normal",family="Century",size=15)
        
        #Front label 
        self.label1 = Label(master,text="Currency Converter",justify=CENTER,font=fonts)
        #self.label1.place(x=10,y=10)
        self.label1.pack()

        #Start Button
        
        self.button = Button(master,text="Start",justify=CENTER,padx=20,pady=20,relief=FLAT,bg="red",command=self.starts)
        self.button.pack(pady=50)
    
    def starts(self):
        
        self.top = Toplevel(self.master)
        self.top.title("Choose an option")
        self.top.geometry("200x200")
        
        self.top.ask_user = Label(self.top,text="What do you want to convert?\n1.Bdt to Dollar\n2.Dollar to Bdt\nPress '1' or '2': ")
        self.top.ask_user.place(x=10,y=20)
        
        
        #Button 1
        self.top.button1 = Button(self.top,text="1",padx=15,pady=12,bg="violet",relief=FLAT,command=self.button1)
        self.top.button1.place(x=40,y=100)
        
        #Button 2
        self.top.button2 = Button(self.top,text="2",padx=15,pady=12,bg="violet",relief=FLAT,command=self.button2)
        self.top.button2.place(x=100,y=100)
        
        
            
    def button1(self):
        print("button 1")
        
        self.button.configure(text="Try Again")
        
        fonts =Font(weight="normal",family="Century",size=20)
        
        #New window
        self.Bdt_to_Dollar = Toplevel(self.master)
        #Window of the Application
        self.Bdt_to_Dollar.title("Bdt to Dollar")
        self.Bdt_to_Dollar.geometry("230x270")
        
        
        #Bdt to Dollar label
        self.Bdt_to_Dollar.label1 = Label(self.Bdt_to_Dollar,text="Bdt to Dollar",font = fonts)
        self.Bdt_to_Dollar.label1.place(x=10,y=30)
        
        
        #Enter value label
        self.Bdt_to_Dollar.label2 = Label(self.Bdt_to_Dollar,text="Enter Bdt TK",font = Font(weight="normal",family="Century",size=12))
        self.Bdt_to_Dollar.label2.place(x=10,y=70)
        
        
        #Entering input
        self.Bdt_to_Dollar.entry1 = Entry(self.Bdt_to_Dollar,font = Font(weight="normal",family="Century",size=12))
        self.Bdt_to_Dollar.entry1.place(x=10,y=120)
        
        
        self.Bdt_to_Dollar.label2 = Label(self.Bdt_to_Dollar,text="",font=fonts) 
        self.Bdt_to_Dollar.label2.place(x=10,y=1500)
        
        
        #Submit button
        
        self.Bdt_to_Dollar.button_submit = Button(self.Bdt_to_Dollar,text="Submit",font = fonts,bg="cyan",command=self.submit_button1)
        self.Bdt_to_Dollar.button_submit.place(x=10,y=200)
        
        self.top.destroy()
        
        
    def button2(self):
        print("button2")
        self.button.configure(text="Try Again")
        
        fonts =Font(weight="normal",family="Century",size=20)
        
        #New window
        self.Dollar_to_Bdt = Toplevel(self.master)
        #Window of the Application
        self.Dollar_to_Bdt.title("Bdt to Dollar")
        self.Dollar_to_Bdt.geometry("230x270")
        
        
        #Bdt to Dollar label
        self.Dollar_to_Bdt.label1 = Label(self.Dollar_to_Bdt,text="Dollar to Bdt",font = fonts)
        self.Dollar_to_Bdt.label1.place(x=10,y=30)
        
        
        #Enter value label
        self.Dollar_to_Bdt.label2 = Label(self.Dollar_to_Bdt,text="Enter Dollar($) value",font = Font(weight="normal",family="Century",size=12))
        self.Dollar_to_Bdt.label2.place(x=10,y=70)
        
        
        #Entering input
        self.Dollar_to_Bdt.entry1 = Entry(self.Dollar_to_Bdt,font = Font(weight="normal",family="Century",size=12))
        self.Dollar_to_Bdt.entry1.place(x=10,y=120)
        
        
        self.Dollar_to_Bdt.label2 = Label(self.Dollar_to_Bdt,text="",font=fonts) 
        self.Dollar_to_Bdt.label2.place(x=10,y=1500)
        
        
        #Submit button
        
        self.Dollar_to_Bdt.button_submit = Button(self.Dollar_to_Bdt,text="Submit",font = fonts,bg="cyan",command=self.submit_button2)
        self.Dollar_to_Bdt.button_submit.place(x=10,y=200)
        
        self.top.destroy()
   
   
    def submit_button1(self):
        try:
            val = int(self.Bdt_to_Dollar.entry1.get()) * 0.012
            self.Bdt_to_Dollar.label2.place(x=10,y=150)
            self.Bdt_to_Dollar.label2.configure(text=str("%.3f"%val)+" dollar")
            self.Bdt_to_Dollar.entry1.delete(0,END)
            print("%.3f"%val,"dollar")
        except Exception as e:
            print(e)
            
        
    def submit_button2(self):
        try:
            val = int(self.Dollar_to_Bdt.entry1.get()) * 84.95
            self.Dollar_to_Bdt.label2.place(x=10,y=150)
            self.Dollar_to_Bdt.label2.configure(text=str("%.3f"%val)+" TK")
            self.Dollar_to_Bdt.entry1.delete(0,END)
            print(val,"TK")
        except Exception as e:
            print(e)
        
        
def main():
    root = Tk()
    app = Currency_Converter(root)    
    root.mainloop()

if __name__ == "__main__":
    main()
   