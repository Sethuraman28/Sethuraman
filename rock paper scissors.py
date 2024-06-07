import random
game=['Rock','Paper','Scissors']
c=p=0
print("Score:\nComputer:"+str(c)+"\nPlayer:"+str(p))
while True:
	comp_choice=random.choice(game)
	command=input("Rock, Paper, Scissors or Quit :")
	if command==comp_choice:
		print("Tie")
	elif command=='Rock':
		if comp_choice=="Paper":
			print("Computer wins!")
			c+=1
		else:
			print("Player wins!")
			p+=1
	elif command=="Paper":
		if comp_choice=="Scissors":
			print("Computer wins!")
			c+=1
		else:
			print("Player wins!")
			p+=1
	elif command=="Scissors":
		if comp_choice=="Paper":
			print("Player wins!")
			p+=1
		else:
			print("Computer wins!")
			c+=1
	elif command=="Quit":
		break
	else:
		print("Wrong command")
	print("Player:"+command)
	print("Computer:"+comp_choice)
	print("\n\nScore:\nComputer:"+str(c)+"\nPlayer:"+str(p))