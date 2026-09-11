
#CodeChallenge#3

print("\t============PACKAGE INFO===========")
name_Sender = input("\n== What is your name == " )
name_Item = input("\n== What would the item Be? == ")
weight = float(input( "\n== How heavy is the Item? ==  "))
distance = float(input( "\n== How far is the distance to be traveled? ==  " ))
is_express = input("\n== Is Item Express? Yes or no ==  ") == "Yes" 
is_international= input("\n== Is Item Internationally shipped? Yes or no ==  ") == "Yes" 
is_Fragile = input("\n== Is Item Fragile? Yes or no ==  ") == "Yes"

base_cost = (weight * 2.50) + (distance * 0.15)



if weight <= 2.0 and distance <= 100 and is_express is False and is_international is False:

	print("\n\n==YOUR ITEM IS FREELY SHIPPED==")
	print("\n============PACKAGE INFO============", "\n","\nItem Weight: ", weight, "kg","\n","Item Distance Travel: ", distance, "km", "\n", "FROM: ", name_Sender, "\n", "Name OF ITEM: ", name_Item)
	print(" ITEM is Fragile ", is_Fragile)
	print("==AMOUNT TOTAL $0==" )


elif is_express is True and is_international is True:

	Total = (base_cost * 1.40) + 50
	print("\n\n==YOUR ITEM IS INTERNATIONALLY EXPRESSED==")
	print("\n============PACKAGE INFO============", "\n","\nItem Weight: ", weight, "kg","\n","Item Distance Travel: ", distance, "km", "\n", "FROM: ", name_Sender, "\n", "Name OF ITEM: ", name_Item)
	print(" ITEM is Fragile ", is_Fragile)
	print("\n==AMOUNT TOTAL = $", Total)

elif is_international is True and weight > 20:

	Total = (base_cost * 1.20) + 25
	print("\n\n==YOUR ITEM IS EXPRESSED OR INTERNATIONALLY==")
	print("\n============PACKAGE INFO============", "\n","\nItem Weight: ","Item Weight: ", weight, "kg","\n","Item Distance Travel: ", distance, "km", "\n", "FROM: ", name_Sender, "\n", "Name OF ITEM: ", name_Item)
	print(" ITEM is Fragile ", is_Fragile)
	print("\n==AMOUNT TOTAL = $", Total)



elif weight > 30 or distance > 1000:
	
	Total = base_cost + 30
	print("\n\n==YOUR ITEM IS OVERSIZED==")
	print("\n============PACKAGE INFO============", "\n","\nItem Weight: ", weight, "kg","\n","Item Distance Travel: ", distance, "km", "\n", "FROM: ", name_Sender, "\n", "Name OF ITEM: ", name_Item)
	print(" ITEM is Fragile ", is_Fragile)
	print("\n==AMOUNT TOTAL = $", Total)



else:
	Total = base_cost
	print("\n\n==STANDARD RATE==")
	print("\n============PACKAGE INFO============", "\n","\nItem Weight: ", weight, "kg","\n","Item Distance Travel: ", distance, "km", "\n", "FROM: ", name_Sender, "\n", "Name OF ITEM: ", name_Item)
	print(" ITEM is Fragile ", is_Fragile)
	print("\n==AMOUNT TOTAL = $", Total)
