n=69
guess=1
while(guess<11):
    a=int(input("Enter your number\n"))

    if (a>n):
        print("Try smaller number")
        print(10-guess,"guesses left\n")
        guess+=1
        continue

    elif(a<n):
        print("Try larger number")
        print(10-guess,"Guesses left\n")
        guess+=1
        continue

    elif(n==a):
        print("Your guess is correct")
        print(guess,"is the number of guesses you took\n")
        break

    
    

if(guess>10):
    print("Game over\n")
    