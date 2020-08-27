#From this website : https://www.madtakes.com/libs/188.html
#Mad Libs Generator with oop python
from tkinter import *
from tkinter.font import Font
class Mad_Libs():
    def __init__(self,main):
        self.main = main
        
        main.title("Mad Libs Generator")
        main.geometry("350x380")
        main.resizable(False,False)
        
        # Be kind ad-Lib
        self.fonts = Font(weight="bold",size=19)
        self.label_1 = Label(main,text="Be Kind ad-Lib",font = self.fonts )
        self.label_1.place(x=80,y=10)
        
        
    #---Adding Parts of speech------------
    
        #Fonts for the labels
        self.label_fonts = Font(family="Tekton Pro",weight="bold",size=15)
        self.entry_fonts = Font(weight="bold",size=10)
        self.random_fonts = Font(weight="normal",size=6)
        
        
        #_________________________NOUN1______________________
        
        #Noun label
        self.noun_label = Label(main,text="Noun",font = self.label_fonts)
        self.noun_label.place(x=15,y=80)
        #Noun Entry field
        self.noun1 = Text(main,height=1,width=22,font= self.entry_fonts)
        self.noun1.place(x=75,y=85)
        #button
        self.button = Button(main,text="Random \n word",font=self.random_fonts,disabledforeground='white',bg="brown4",state=DISABLED,width=6)
        self.button.place(x=245,y=82)
        
        
        #Totally Random button
        self.button = Button(main,text="Totally \n random",font=Font(weight="bold",size=6),disabledforeground='white',bg="slateblue3",state=DISABLED)
        self.button.place(x=297,y=82)
        
        
        #_________________________NOUN(PLURAL)2______________________
        
        #Noun(Plural) label
        self.noun_label = Label(main,text="Noun(Plural)",font = Font(weight="bold",size=10,family="Tekton Pro"))
        self.noun_label.place(x=5,y=120)
        #Noun Entry field
        self.noun2 = Text(main,height=1,width=22,font= self.entry_fonts)
        self.noun2.place(x=75,y=125)
        #button
        self.button = Button(main,text="Random \n word",font=self.random_fonts,disabledforeground='white',bg="brown4",state=DISABLED,width=6)
        self.button.place(x=245,y=122)
        
        
        
        #_________________________NOUN3______________________
        
        #Noun label
        self.noun_label = Label(main,text="Noun",font = self.label_fonts)
        self.noun_label.place(x=15,y=160)
        #Noun Entry field
        self.noun3 = Text(main,height=1,width=22,font= self.entry_fonts)
        self.noun3.place(x=75,y=165)
        #button
        self.button = Button(main,text="Random \n word",font=self.random_fonts,disabledforeground='white',bg="brown4",state=DISABLED,width=6)
        self.button.place(x=245,y=162)
        
        
        #_________________________Place______________________
        
        #Noun label
        self.noun_label = Label(main,text="Place",font = self.label_fonts)
        self.noun_label.place(x=15,y=200)
        #Noun Entry field
        self.places = Text(main,height=1,width=22,font= self.entry_fonts)
        self.places.place(x=75,y=205)
        #button
        self.button = Button(main,text="Random \n word",font=self.random_fonts,disabledforeground='white',bg="brown4",state=DISABLED,width=6)
        self.button.place(x=245,y=202)
        
        
        #_________________________ADJECTIVES______________________
        
        #Noun label
        self.noun_label = Label(main,text="Adjective",font = Font(weight="bold",size=12,family="Tekton Pro"))
        self.noun_label.place(x=8,y=240)
        #Noun Entry field
        self.adj = Text(main,height=1,width=22,font= self.entry_fonts)
        self.adj.place(x=75,y=245)
        #button
        self.button = Button(main,text="Random \n word",font=self.random_fonts,disabledforeground='white',bg="brown4",state=DISABLED,width=6)
        self.button.place(x=245,y=242)
        
        
        #_________________________NOUN4______________________
        
        #Noun label
        self.noun_label = Label(main,text="Noun",font = self.label_fonts)
        self.noun_label.place(x=15,y=280)
        #Noun Entry field
        self.noun4 = Text(main,height=1,width=22,font= self.entry_fonts)
        self.noun4.place(x=75,y=285)
        #button
        self.button = Button(main,text="Random \n word",font=self.random_fonts,disabledforeground='white',bg="brown4",state=DISABLED,width=6)
        self.button.place(x=245,y=282)
    
        #_________________________Go Mad button______________________
    
        self.go_mad = Button(main,text="Go Mad!",bg="slate blue",fg="white",font=Font(size=10),command=self.go_mad)
        self.go_mad.place(x=130,y=328)
        
#Go Mad Libs Function
    def go_mad(self):
        noun1 =  self.noun1.get("1.0","end-1c") 
        self.noun1.delete("1.0",END)
        noun2 = self.noun2.get("1.0","end-1c") 
        self.noun2.delete("1.0",END)
        noun3 = self.noun3.get("1.0","end-1c") 
        self.noun3.delete("1.0",END)
        places = self.places.get("1.0","end-1c") 
        self.places.delete("1.0",END)
        adj = self.adj.get("1.0","end-1c") 
        self.adj.delete("1.0",END)
        noun4 = self.noun4.get("1.0","end-1c") 
        self.noun4.delete("1.0",END)
        
        all_text = "Be kind to your {} -footed {}\nFor a duck may be somebody`s {},\nBe kind to your {} in {}\nWhere the weather is always {}.\n\nYou may think that this is the {},\nWell it is.".format(noun1,noun2,noun3,noun2,places,adj,noun4)
        
        new_window = Toplevel(self.main,height=200,width=350)
        self.all_ = Label(new_window,text=all_text,font=Font(size=15))
        self.all_.place(x=10,y=10)
        
        print("Success")


#Main Tkinter 
def madlibs_generator():
    root = Tk()
    app = Mad_Libs(root)
    root.mainloop()
    
if __name__ == "__main__":
    #mad = Mad_Libs("k").mad_libs_story()
    #print(mad)
    madlibs_generator()
    
