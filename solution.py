userInput=int(input("Enter a value to see if it is a prime number: "))
counter=1

while(counter<userInput):
    if(userInput%counter == 0 and counter!=1): 
        print("prime im not")
    counter=counter+1

if(counter==userInput): 
    print("prime i am")
