from utils import save_password, retrieve_password

print("Welcome to LockyBear! I am going to help you manage passwords! 🐻")

message_1 = input("type 1 for saving password, 2 for retrieving password")

if message_1 == "1":
    entity_name = input("What account do you want to save the password of? ")
    password = input("What is your password for this account? ")
    save_password(entity_name, password)

elif message_1 == "2":
    entity_name = input("What account do you want to retrieve the password of? ")
    retrieve_password(entity_name)
