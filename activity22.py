
kuroko = ["Phantom Sixth Man", "Misdirection"]
kagami = ["Seirin's ace", "Jumping ability"]
aomine = ["Unpredictable scorer", "Street basketball"]
akashi = ["Team captain", "Emperor Eye"]
midorima = ["High accuracy shooter", "Three-point shots"]
kise = ["Copy ability", "Perfect Copy"]
murasakibara = ["Defensive powerhouse", "Great strength"]

gojo = ["Strongest jujutsu sorcerer", "Limitless"]
yuji = ["Jujutsu student", "Divergent Fist"]

curry = ["Point Guard", "Elite three-point shooter"]
durant = ["Small Forward", "Scoring ability"]
kobe = ["Shooting Guard", "Fadeaway"]
jordan = ["Shooting Guard", "Mid-range scoring"]
lebron = ["Small Forward", "Powerful drive"]

kuroko_no_basket = {
    "Kuroko": kuroko,
    "Kagami": kagami,
    "Aomine": aomine,
    "Akashi": akashi,
    "Midorima": midorima,
    "Kise": kise,
    "Murasakibara": murasakibara}

jujutsu_kaisen = {
    "Gojo": gojo,
    "Yuji": yuji}

nba = {
    "Stephen Curry": curry,
    "Kevin Durant": durant,
    "Kobe Bryant": kobe,
    "Michael Jordan": jordan,
    "LeBron James": lebron}

sports = {"Kuroko no Basket": kuroko_no_basket}
shonen = {"Jujutsu Kaisen": jujutsu_kaisen}
basketball = {"Players": nba}

anime = {
    "Sports Anime": sports,
    "Shonen": shonen,
    "NBA": basketball}

print("=== 1. Going down one level at a time ===")
print(anime["Sports Anime"]["Kuroko no Basket"]["Kuroko"][1])

print()
print("=== 2. Loop level 1: categories ===")

for category in anime:
    print(category)

print()
print("=== 3. Loop levels 1-2: categories and titles ===")

for category, titles in anime.items():
    print(category)
    for title in titles:
        print(" -", title)

print()
print("=== 4. Loop ALL levels ===")

for category, titles in anime.items():
    print(category)
    for title, characters in titles.items():
        print("  " + title)
        for name, info in characters.items():
            print("    " + name)
            print("      Description:", info[0])
            print("      Power:", info[1])

print()
print("=== 5. Count every character ===")

count = 0

for titles in anime.values():
    for characters in titles.values():
        for name in characters:
            count = count + 1

print("Total characters:", count)

print()
print("=== 6. Search for a character ===")

search = "Stephen Curry"
found = False

for category, titles in anime.items():
    for title, characters in titles.items():
        if search in characters:
            print(search, "is from", title, "(" + category + ")")
            print("Power:", characters[search][1])
            found = True

if found == False:
    print(search, "not found.")
