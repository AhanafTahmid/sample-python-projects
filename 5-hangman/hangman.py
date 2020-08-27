#Hangman trying with oop .
import random
import sys
c = 0 #Counnting if input word matches the actual word
if_not_matches = 0
class Hangman:
    def __init__(self,word):
        self.word = word
    def __str__(self):
        return self.word
    def get_num(self):
        #return self.word + " hey"
        return f"{self.word}"
        
    def get_length(self):
        return len(self.word)
    
    def get_matched(self,input_word):
        self.iw = input_word
        #input_word = [i for i in input("Please Enter a word : \n").split()]
        #Check if word matches
        """ if self.word==self.iw:
            return "Yes"
        else:
            return "No" """
        
        
         #Hangman list
        Hangman_list =  ['''
   +---+

   |   |

       |
       |
       |
       |

 =========''', '''

   +---+

   |   |

   O   |

       |

       |

       |

 =========''', '''

   +---+

   |   |

   O   |

   |   |

       |

       |

 =========''', '''

   +---+

   |   |

   O   |

  /|   |

       |

       |

 =========''', '''

   +---+

   |   |

   O   |

  /|\  |

       |

       |

 =========''', '''

   +---+

   |   |

   O   |

  /|\  |

  /    |

       |

 =========''', '''

   +---+

   |   |

   O   |

  /|\  |

  / \  |

       |

 =========''']
        
        
        
        
        #If the word is available in the list
        list_to_str = "".join(input_word)
        
        if list_to_str in list(self.word):
            global c
            c = c+1 
            if c==4:
                #return "Great Job! Got all the words"
                sys.exit("Great Job! Got all the words.\nThe word was %s"%random_words)
            return "Yes"
        else:
            global if_not_matches
            if_not_matches = if_not_matches+1
            if if_not_matches >=7:
                sys.exit("Bye .Too many attempts")
        return "No \t \t %s"%Hangman_list[if_not_matches] 
    
       
            

if __name__== "__main__":
    #get_length = Hangman("king").get_length()
    #var_match = Hangman("king").match()
    
    #For muliple inputs
    for k in range(9):
        words = ["King","Queen","Jack","Lack","Pack","Fake","Lake","Bake","Take","Check"]
        random_words = random.choice(words)
        see_if_matches= Hangman(random_words).get_matched(input("Please Enter a word : \n"))
        #print(6-k,"attepts left")
        print(see_if_matches)
        
    
    
    