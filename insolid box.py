n = 5


for x in range (n):
    for y in range (n):
        if x == 0 or y == 0 or x == 4 or y == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print() 
     



