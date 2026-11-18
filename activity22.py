fruits = ["apple", "banana", "cherry", "date", "fig", "grape"]

print(fruits[-1]) 
fruits_d = {"Bilog_m": "longgan", "maasim": "lipute"}
print(fruits_d["Bilog_m"])

#2d list
Lakers = ["Lebron", "Davis", "Westbrook", "Caldwell-Pope"]
Celtics = ["Tatum", "Brown", "Smart", "Horford"]
old_teams = [Lakers, Celtics]
new_teams = ["Misamis heat", "San Antonio Brgy.12", "Washington Candelaria", "Huskers", "Stolen Gate Warroirs"]

laban = [{"Mamaw": old_teams, "new_teams": new_teams}]

print(laban[0]["Mamaw"][0][1])
print(laban[0]["new_teams"][2])




