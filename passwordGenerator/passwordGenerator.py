import passwordClass as pwd
from datetime import date, timedelta

if __name__ == "__main__":
   #input and/or output file (include input data with your project)
   l = int(input("What is the required length of the password? "))
   n = int(input("How many numbers are required? "))
   s = int(input("How many special characters are required? ")) 

   #Using Tuple
   lns = tuple((l,n,s))

   pasw = pwd.Password(lns)
   gen_password = pasw.genPassword()
   print("\nYour password is:", gen_password)
   
   current_date = date.today().isoformat()   
   days_after = (date.today()+timedelta(days = 60)).isoformat() 
   print("\nToday's Date:", current_date)
   print("Password Expiration Date:", days_after)
    
   try :
        f = open("password.txt",'a+')      
        f.write("Password: " + gen_password)
        f.write('\n')
        f.write("Today's Date: " + current_date)
        f.write('\n')
        f.write("Expiration Date: " + days_after)
        f.close()
   except FileNotFoundError:
       print('File Does Not Exist')
       quit()

