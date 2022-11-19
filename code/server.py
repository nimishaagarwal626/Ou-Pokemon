import random
import numpy
 
def createBoard():

    with open('contents.txt', 'r') as f:
        values = f.readlines()

    noOfTrainers = int(values[0])
    noOfPokemons = int(values[1])
    n = int(values[2])
    trainers=["🧠","🫀","🫁" ,"🦷" ,"🦴","👁️","👅" ,"👄"] 
    matrix = numpy.empty(shape=(n, n), dtype='object')
    countpokemon=0
    counttrainer=0
    pokemons = []
    trainers = []
    with open('pokemons_emojis.txt', 'r') as p:
        pokemons = p.readlines()
    pok = [x[:-1] for x in pokemons]

    with open('trainers_emojis.txt', 'r') as t:
        trainers = t.readlines()
    trainer = [x[:1] for x in trainers]

    while countpokemon<=noOfPokemons-1:
        randomrow=random.choice(range(0,n))
        randomcolumn=random.choice(range(0,n))
        if matrix[randomrow][randomcolumn]==None:
            emoji=random.choice(pok)
            matrix[randomrow][randomcolumn]= emoji
            pok.remove(emoji)
            countpokemon+=1
    while counttrainer<=noOfTrainers-1:
        randomrow=random.choice(range(0,n))
        randomcolumn=random.choice(range(0,n))
        if matrix[randomrow][randomcolumn]==None:
            emoji=random.choice(trainer)
            matrix[randomrow][randomcolumn]= emoji
            trainer.remove(emoji)
            counttrainer+=1
    print(matrix)


if __name__=='__main__':
    createBoard()