#basic if else 
import getpass

username = "user1"
password = "araykopo1"

u = input("input USERNAME ====>") 
p = getpass.getpass("input PASSWORD ====>")

if u == username:
	print(" => Hello ", username, " <= ")
else:
	print(" => Wrong USERNAME <= ")

if p== password:
	print(" => Correct PASSWORD <= ")
else:
	print(" => Wrong PASSWORD <= ")




