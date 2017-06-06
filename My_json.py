import json

f = open('My_Json.txt', 'w')
player1 = {
    'Name': 'Ramon',
    'Score': '456',
    'Skills': ['Strent', 'GodMode']
}

player2 = {
    'Name': 'Patrik',
    'Score': '500',
    'Skills': ['Invisibility', 'IronFist']
}

z = [player1,  player2]

json.dump(z, f)

f.close()

f = open('My_Json.txt', mode='r')

json_data = json.load(f)

for user in json_data:
    print('Player name is: ' + str(user['Name']))
    print('Player score is: ' + str(user['Score']))
    print('Player skills is: ' + str(user['Skills']))

# And this is really good and proper work version