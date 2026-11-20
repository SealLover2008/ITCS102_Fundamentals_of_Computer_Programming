
#Anime and NBA list Dictionary

kuroko_no_basket = {
    "Kuroko": ["Phantom Sixth Man", "Misdirection"],
    "Kagami": ["Seirin's ace", "Jumping ability"],
    "Aomine": ["Unpredictable scorer", "Street basketball"],
    "Akashi": ["Team captain", "Emperor Eye"],
    "Midorima": ["High accuracy shooter", "Three-point shots"],
    "Kise": ["Copy ability", "Perfect Copy"],
    "Murasakibara": ["Defensive powerhouse", "Great strength"]}

anime = {}
anime["Sports Anime"] = {"Kuroko no Basket": kuroko_no_basket}
sports = {"Kuroko no Basket": kuroko_no_basket}
anime["Sports Anime"] = sports

jjk = ["Gojo", "Strongest jujutsu sorcerer", "Limitless"]
anime["Shonen"] = {"Jujutsu Kaisen": jjk}


nba = {
    "Stephen Curry": ["Point Guard", "Elite three-point shooter"],
    "Kevin Durant": ["Small Forward", "Scoring ability"],
    "Kobe Bryant": ["Shooting Guard", "Fadeaway"],
    "Michael Jordan": ["Shooting Guard", "Mid-range scoring"],
    "LeBron James": ["Small Forward", "Powerful drive"]}
anime["NBA"] = {"Players": nba}
anime["Sports Anime"]["Kuroko no Basket"]["Kuroko"][1] = "Vanishing Drive"
anime["NBA"]["Players"]["Stephen Curry"][1] = "Deep three-point shooting"
curry = ["Point Guard", "Elite three-point shooter"]
nba["Stephen Curry"] = curry

print(anime["NBA"]["Players"]["LeBron James"])
print(anime["Shonen"])
print(anime["Sports Anime"]["Kuroko no Basket"]["Midorima"])
