import random as r 
print("\t\t\t  GUESS GAME")
i=int(input("Enter the number of guesses you wanna take:")) 
play=0
win=lose=0
a=r.randint(1,10)
while play<i:
	b=int(input("\nEnter a number between 1 and 10:"))
	if b==a:
		print("Yay! \nYou guessed the number!!!")
		win+=1
		play+=1
		break
	else:
		print("Your guess is wrong!\nTry again!")
		if(b<a+3 and b>a-3):
			print("You are so close")
		lose+=1
		play+=1
