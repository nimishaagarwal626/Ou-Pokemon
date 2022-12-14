from __future__ import print_function
 
from ruamel import yaml

VERSION = {'version':'3.7'}
SERVICES = {'server': 'server'}

#Taking user inputs
noOfTrainers = input('Enter the number of Trainers:')
noOfPokemons = input('Enter the number of Pokemons:')
boardsize=input("Enter the size of board:")
numOfTrainers=int(noOfTrainers)
numOfPokemons=int(noOfPokemons)

#Writing the inputs into contents.txt file to access it in node.py
f = open('contents.txt', 'w+')
f.write(noOfTrainers + '\n')
f.write(noOfPokemons + '\n')
f.write(boardsize)

for i in range(numOfTrainers):
    SERVICES["client"+str(i)] = "Trainer"+str(i)
 
for j in range(numOfPokemons):
    SERVICES["client"+str(i+j+1)] = "Pokemon"+str(j)
 
COMPOSITION = {'services': {}}
 
#Adding these fields to every container
def servicize(name, image):
    entry = {
            'build': '.',
            'hostname': image,
            'container_name': image,
            'networks': ['default']}
    return entry
 
if __name__ == '__main__':
    for name, image in SERVICES.items():
        COMPOSITION['services'][name] = servicize(name, image)
    print(yaml.dump(COMPOSITION, default_flow_style=False, indent=4), end='')
    
    #generating docker-compose.yml
    with open('docker-compose.yml', 'w+') as outfile:
        yaml.dump(VERSION, outfile, default_flow_style=False, indent=4)
        yaml.dump(COMPOSITION, outfile, default_flow_style=False, indent=4)
    