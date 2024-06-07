string=str(input("Enter a sentence:"))
vowels=0
consonants=0
spaces=0
upper_cases=0
lower_cases=0
words=0
for x in string:
	if x in ('A','a','E','e','I','i','O','o','U','u'):
		vowels+=1
	if x not in ('A','a','E','e','I','i','O','o','U','u'):
		consonants+=1
	if x==" ":
		spaces+=1
		words+=1
	if x.isupper():
		upper_cases+=1
	if x.islower():
		lower_cases+=1
    
print(f"The sentence '{string}' contains........" )
print(vowels,"vowels")
print(consonants,"consonants")
print(spaces,"spaces")
print(upper_cases,"upper cases")
print(lower_cases,"lower cases")
print(words+1,"words")
print("And the length of the string is ",len(string))

	