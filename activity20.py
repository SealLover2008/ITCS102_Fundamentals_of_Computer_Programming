anime = []

isContinuing = True

while isContinuing:
    ans = input("Do you want to add a title of an anime (y/n): ") == "y"
    if ans == True:
        title = input("Enter the title of an anime: ")
        anime.append(title)
        ans = input("Do you want to add another title of an anime (y/n): ") == "y"
      
    else:
        isContinuing = False
        print(anime)

