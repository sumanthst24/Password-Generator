import random#import random module
import sys#import sys module
def Password_Generator():
    length=random.randrange(8,13)#generate length of password
    #print(length)
    password=""#initialise the password
    password_length=1#initialise the password length 
    symbols_range=[33,47]#ascii range for symbols
    numbers_range=[48,57]#ascii range for digits
    lowercase_range=[97,122]#ascii range for lowercase letters
    uppercase_range=[65,90]#ascii range for uppercase letters
    while(password_length<=length):
        choice=random.randrange(1,5)#generation of random choice
        #print("choice",choice)
        if(choice==1):
            generated=random.randrange(symbols_range[0],symbols_range[1])#generate a random symbol ascii value
            password=password+chr(generated)#add the character to the password
        elif(choice==2):
            generated=random.randrange(numbers_range[0],numbers_range[1])#generate a random digits ascii value
            password=password+chr(generated)#add the character to the password
        elif(choice==3):
            generated=random.randrange(lowercase_range[0],lowercase_range[1])#generate a random lowercase letter ascii value
            password=password+chr(generated)#add the character to the password
        elif(choice==4):
            generated=random.randrange(uppercase_range[0],uppercase_range[1])#generate a random upper case letter ascii value
            password=password+chr(generated)#add the character to the password
        password_length=password_length+1#increment by the password length by 1
        #print(password)
    return password#return the length when the password length becomes the generated password length
            
            
            
    

print("This program generates a password of at least 8 characters and 12 characters at maximum level")
print("Choose your option")#display the options
print("1.Generate the password")
print("2.Exit the program")
n=input()

if(int(n)<1 and int(n)>2):#invalid choice
        print("Invalid Option")
        sys.exit()
elif(n=='1'):
        print("Generating a password")
        generated=Password_Generator()#call startGame() function
        print("The password generated is "+generated)
elif(n=='2'):
            sys.exit()#exit
else:
        print("You selected an invalid option")
        sys.exit()#exit
