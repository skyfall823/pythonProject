import random

#  User-defined function
def randomDigit():
   i=random.randint(0,9)    
   #list
   DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  
   return DIGITS[i]

def randomLetter():
   i=random.randint(0,51)       
   LETTER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
             'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q',
             'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z', 
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
             'I', 'J', 'K','L', 'M', 'N', 'O', 'P', 'Q',
             'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
   return LETTER[i]
def randomSymbols():
   i=random.randint(0,7) 
      
   SYMBOLS = ['!','@','#','$','%','^','&','*']
   return SYMBOLS[i]

# User-defined class
class Password:
   __password = '********' 

   def __init__(self, lns ):
       self.length= lns[0]     
       self.num=lns[1]            
       self.special=lns[2]    

   def __repr__(self):
       return f'Class Password(({self.length},{self.num},{self.special}))'
   
   def __add__(self, other):
       self.length+=other.length     
       self.num+=other.num            
       self.special+=other.special  
       return self.__password+other.__getpassword()

   def __getpassword(self):
       return self.__password

   def genPassword(self):
       pasw=""
       try:           
            num_char=set()           
            i=0
            while i < self.num:
                num_char.add(randomDigit())
                i=len(num_char)
            
            # Using Set 
            special_char=set()

            i=0
            while i < self.special:
                special_char.add(randomSymbols())
                i=len(special_char)

            alfa_len= self.length- self.num- self.special

            alphabet_char=set()
            i=0
            while i < alfa_len:
                alphabet_char.add(randomLetter())
                i=len(alphabet_char)
                
            # Using Dictionary
            all_char={0:alphabet_char,1:num_char,2:special_char}  

            # Adding special characters in password 
            l=0
            pwd=[]
            while( l<= self.length-1 ):
                r=random.randint(0,2)
                Set=all_char.get(r)
                if len(Set)==0:
                    continue
                pwd.append( Set.pop() )
                l+=1

            pasw=''.join(map(str, pwd))

       except:
           print("Password Not Generated!!")
       else:
           self.__password=pasw
       
       return self.__getpassword()

def test_class():
    # Testing password length, num=0 and special=0
    lns=(4,0,0)

    pwd = Password(lns)
    print("__init()__ Test Completed.")

    assert 'Class Password((4,0,0))' == repr(pwd) , "__repr()__ Test Failed."
    print("__repr()__ Test Completed.")

    pas=pwd.genPassword()
    assert pas.isalpha() == True , "genPassword() Test Failed."
    print("genPassword() Test Completed.")
    
    lns=(3,0,0)
    _pwd = Password(lns)
    _pwd.genPassword()
    add_pass=_pwd+pwd
    assert add_pass.isalpha() and len(add_pass)==7 , "__add__() Test Failed."
    print("__add__() Test Completed.")

    print("Password Class Test Completed; ALL methods Are Working Correctly.")

if __name__ == "__main__":
    test_class()