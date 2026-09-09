#Multiple if and elif conditions

#Create a python program that would capture a age group 

Name = input("Please input your name ----> ")

age= int(input("Please input your age ----->"))



if age >= 0 and age <= 5: 
	print("You are considerd as an INFANT")

elif age >= 6 and age <= 12: 
	print("You are considerd as an KID")

elif age >= 13 and age <= 15: 
	print("You are considerd as an PRE-TEEN")

elif age >= 16 and age <= 19: 
	print("You are considerd as an TEEN")

elif age >= 20 and age <= 29: 
	print("You are considerd as an EARLY ADULTHOOD")

elif age >= 30 and age <= 58: 
	print("You are considerd as an ADULT")

elif age >= 59 and age <= 150: 
	print("You are considerd as an SENIAL SENIOR")


else:
	print("Invalid Age/SKELETON YERN?")