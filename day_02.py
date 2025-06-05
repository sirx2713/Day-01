heartbeat_numbers = input("Enter her numbers: ")

if heartbeat_numbers == 778653649:
    print("You know her numbers by heart!")
elif heartbeat_numbers != 778653649:
    print("You are such a scam!")

heartbeat_name = input("Enter her name: ")

if heartbeat_name == "Tinotenda" or heartbeat_name == "Wendy":
    print("You are a soulmate!")
    print('T' in heartbeat_name)
    print('W' in heartbeat_name)

elif heartbeat_name != "Tinotenda" or heartbeat_name != "Wendy":
    print("You are such a loser!")
    print('T' not in heartbeat_name)
    print('W' not in heartbeat_name)