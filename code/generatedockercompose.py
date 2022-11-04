from __future__ import print_function
 
from ruamel import yaml

VERSION = {'version':'3.7'}
SERVICES = {'server': 'server'}
numOfTrainers=int(input('Enter the number of Trainers:'))
numOfPokemons=int(input('Enter the number of Pokemons:'))
for i in range(numOfTrainers):
    SERVICES["client"+str(i)] = "Trainer"+str(i)
 
for j in range(numOfPokemons):
    SERVICES["client"+str(i+j+1)] = "Pokemon"+str(j)
 
COMPOSITION = {'services': {}}
 

def servicize(name, image):
    entry = {'build':".",
             'hostname': image,
             'container_name': image,
             'networks': ['default']}
    return entry
 

if __name__ == '__main__':
    for name, image in SERVICES.items():
        COMPOSITION['services'][name] = servicize(name, image)
    print(yaml.dump(COMPOSITION, default_flow_style=False, indent=4), end='')
    with open('docker-compose.yml', 'w+') as outfile:
        yaml.dump(VERSION, outfile, default_flow_style=False, indent=4)
        yaml.dump(COMPOSITION, outfile, default_flow_style=False, indent=4)
    