import random as r
def handcricket():
	a="bat","bowl"
	comp_batbowl=r.choice(a)
	even_odd=input("Odd or Even:")
	comp_choice=r.randint(1,10)
	sum=0
	while True:
		if even_odd=="odd" or even_odd=="ODD" or even_odd=="Odd":
			print("Hai!")
			n=int(input("Enter a number from 1 to 10:"))
			if n<=10:
				num=n+comp_choice
				if num%2==0:
					print("Computer won the toss!!!")
				else:
					print("You won the toss!!!")
					sum+=1
			else:
				print("Invalid Input!!!\nStart the game from beginning")
				handcricket()
		elif even_odd=="even" or even_odd=="EVEN" or even_odd=="Even":
			print("Hello")
			n=int(input("Enter a number from 1 to 10:"))
			num=n+comp_choice
			if num%2==0:
				print("You won the toss!!!")
				sum+=1
			else:
				print("Computer won the toss!!!")
		else:
			print("Invalid Input!!!")
		break

	if sum==0:      #computer chooses whether to bat or bowl
	
	
		if comp_batbowl=="bat":       #chooses bat
			print("Computer chose to bat first!!!")	
			run=0
			while True:				
				Run=r.randint(1,10)
				bowl=int(input("Bowl:"))
				if bowl<=10:
					if bowl!=Run:
						run+=Run
						print(run,Run)
					elif bowl==Run:
						print(f"Computer got out at {run} runs")
						break
				else:
					print("Invalid Input!!!\nStart the game from beginning")
					handcricket()
			print("Your target is {} runs".format(run+1))
			
			batrun=0
			print("Your turn to bat!!!\U0001F600")
			while batrun<=run:
				Bowl=r.randint(1,10)
				bat=int(input("Bat:"))
				if bat<=10:
					if bat!=Bowl:
						batrun+=bat
						print(batrun,Bowl)
					elif bat==Bowl:
						print("GAME OVER!!! \n You lose the match and computer wins! \nBetter luck next time!")
						break
				else:
					print("Invalid Input!!!\nStart the game from beginning")
					handcricket()
			else:
				print("YAY! You won the game!\a CONGRATS!")
			play=int(input("If you wanna play the game again press 1 or if you wanna quit press any 0 and enter:"))
			if play==1:
				handcricket()
			else:
				print("THANK YOU!!!")
	
	
		elif comp_batbowl=="bowl":    #chooses bowl
			batrun=0
			print("Computer won the toss and chose to bowl first!!!\nYou have to bat first!\U0001F600")
			while batrun>=0:
				Bowl=r.randint(1,10)	
				bat=int(input("Bat:"))
				if bat<=10:
					if bat!=Bowl:
						batrun+=bat
						print(batrun,Bowl)
					elif bat==Bowl:
						print(f"You got out at {batrun} runs!")
						print("Computer's target is {} runs!".format(batrun+1))
						break
				else:
					print("Invalid Input!!!\nStart the game from beginning")
					handcricket()
				
			run=0
			print("Computer's turn to bat!!!")	
			while run<=batrun:
				Run=r.randint(1,10)				
				bowl=int(input("Bowl:"))
				if bowl<=10:
					if bowl!=Run:
						run+=Run
						print(run,Run)
					elif bowl==Run:
						print(f"Computer got out at {run} runs\nYay! You won the game!")
						break
				else:
					print("Invalid Input!!!\nStart the game from beginning")
					handcricket()
			else:
				print("Yay! \nComputer won the match!")
			play=int(input("If you wanna play the game again press 1 or if you wanna quit press 0 and enter:"))
			if play==1:
				handcricket()
			else:
				print("THANK YOU!!!")
		
	else: #player has to choose whether to bat or bowl
		c=str(input("Bat or Bowl:"))
		if c=="bat":
			batrun=0
			print("You chose  to bat first!")
			while batrun>=0:
				Bowl=r.randint(1,10)
				bat=int(input("Bat:"))
				if bat<=10:
					if bat!=Bowl:
						batrun+=bat
						print(batrun,Bowl)
					elif bat==Bowl:
						print(f"You got out at {batrun} runs!")
						print("Computer's target is {} runs!".format(batrun+1))
						break
				else:
					print("Invalid Input!!!\nStart the game from beginning")
					handcricket()
					
			
			run=0
			print("Computer's turn to bat!!!")
			while run<=batrun:
				Run=r.randint(1,10)			
				bowl=int(input("Bowl:"))
				if bowl<=10:
					if bowl!=Run:
						run+=Run
						print(run,Run)
					elif bowl==Run:
						print(f"Computer got out at {run} runs\nYou won the match \nCongrats.........")
						break
				else:
					print("Invalid Input!!!\nStart the game from beginning")
					handcricket()
			else:
				print("Yay! \nComputer won the match!")
			
			play=int(input("If you wanna play the game again press 1 or if you wanna quit press 0 and enter:"))
			if play==1:
				handcricket()
			else:
				print("THANK YOU!!!")
	
		elif c=="bowl":
			run=0
			print("You chose to bowl first!!!")
			while run>=0:
				Run=r.randint(1,10)
				bowl=int(input("Bowl:"))
				if bowl<=10:
					if bowl != Run:
						run+=Run
						print(run,Run)
					elif bowl==Run:
						print(f"Computer got out at {run} runs")
						print("Your target is {} runs".format(run+1))
						break
				else:
					print("Invalid Input!!!\nStart the game from beginning")
					handcricket()

			batrun=0
			print("Your turn to bat!!!\U0001F600")
			while batrun<=run:
				Bowl=r.randint(1,10)
				bat=int(input("Bat:"))	
				if bat<=10:
					if bat != Bowl:
						batrun+=bat
						print(batrun,Bowl)
					elif bat==Bowl:
						print(Bowl)
						print("GAME OVER!!! \n You lose the match and computer wins! \nBetter luck next time!")
						break
				else:
					print("Invalid Input!!!\nStart the game from beginning")
					handcricket()
			else:			
				print("Yay!!! You won the match!")
			play=int(input("If you wanna play the game again press 1 or if you wanna quit press 0 and enter:"))
			if play==1:
				handcricket()
			else:
				print("THANK YOU!!!")
		
	print("Thank you for playing this game!!!\nHope it was interesting!\U0001F600")
	
handcricket()
