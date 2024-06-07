import random
words=["computer","laptop","windows","desktop"]
word=random.choice(words)
print("Guess the character:")
guesses=" "
turns=3
while turns>0:
	failed=0
	for char in word:
 		if char in guesses:
 			print(char)
 		else:
 			print("_")
 			failed+=1
	if failed==0:
		print('You win')
		print("The word is ",word)
	guess=input("Guess the character:")
	guesses+=guess
	if guess not in word:
 		turns-=1
 		print("Wrong\nYou have ",(turns), "more guesses")
	if turns==0:
 		print("Sorry", (name),". You lost, the secret word was ",(word))
	

