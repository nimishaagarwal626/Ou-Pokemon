from concurrent import futures
import grpc
import random
import numpy
import pokemonou_pb2 as pb2
import pokemonou_pb2_grpc as pb2_grpc
import time
import socket
import threading
import math
import sys

class OUPokemanGameServicer(pb2_grpc.OUPokemanGameServicer):
    def __init__(self, start = 0):
        self.lock = threading.Lock()
        self.value = start

    def Board(self, request, context):
        for row in matrix:
            spaciousMatrix = "  ".join(map(str,row))
            print(spaciousMatrix)
        hostname = request.name
        exist = ""
        if(hostname.startswith("Pok")):
            if hostname in initial_moves:
                exist = True
        return pb2.InitialMoves(exist = str(exist))

    def PokemonMove(self, request, context):
        self.lock.acquire()
        self.value = self.value + 1
        global countPokemon 
        msg = movePokemon(request.hostname)
        if msg == "captured":
            countPokemon = countPokemon + 1
        self.lock.release()
        return pb2.Message(count = countPokemon)

    def TrainerMove(self, request, context):
        self.lock.acquire()
        self.value = self.value + 1
        global count 
        msg = moveTrainer(request.hostname)
        if msg == "captured":
            count = count + 1
        self.lock.release()
        return pb2.Message(count = count)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    pb2_grpc.add_OUPokemanGameServicer_to_server(OUPokemanGameServicer(), server)
    server.add_insecure_port("0.0.0.0:50051")
    server.start()
    hostname = socket.gethostname()
    if(socket.gethostname() == 'server'):
        createBoard()
    if(hostname != 'server'):
        time.sleep(10)
        run(hostname)
    server.wait_for_termination()

def createBoard():
    global initial_moves
    global list1
    global list2
    initial_moves={}
    countpokemon=0
    counttrainer=0
    pokemons = []
    trainers = []
    list1 = []
    list2 = []
    
    with open('pokemons_emojis.txt', 'r') as p:
        pokemons = p.readlines()
    pok = [x[:-1] for x in pokemons]

    with open('trainers_emojis.txt', 'r') as t:
        trainers = t.readlines()
    trainer = [x[:1] for x in trainers]
    
    while countpokemon<=noOfPokemons-1:
        randomrow=random.choice(range(0,n-1))
        randomcolumn=random.choice(range(0,n-1))
        if matrix[randomrow][randomcolumn]=="🔷":
            emoj=random.choice(pok)
            matrix[randomrow][randomcolumn]= emoj
            initial_moves["Pokemon"+str(countpokemon)] = (randomrow,randomcolumn)
            pok.remove(emoj)
            countpokemon+=1 

    while counttrainer<=noOfTrainers-1:
        randomrow=random.choice(range(0,n))
        randomcolumn=random.choice(range(0,n))
        if matrix[randomrow][randomcolumn]=="🔷":
            emoj=random.choice(trainer)
            matrix[randomrow][randomcolumn]= emoj
            initial_moves["Trainer"+str(counttrainer)] = (randomrow,randomcolumn)
            trainer.remove(emoj)
            counttrainer+=1

    for row in matrix:
            spaciousMatrix="  ".join(map(str,row))
            return spaciousMatrix

def run(hostname):
    sys.setrecursionlimit(1000)
    with grpc.insecure_channel('server:50051') as channel:
        stub = pb2_grpc.OUPokemanGameStub(channel)   
        print("Requesting Board....")
        res = stub.Board(pb2.Hostname(name=hostname))
        if(hostname.startswith("Pok")):
            if(res.exist == str(True)):
                print("Pokemon is moving")
                res = stub.PokemonMove(pb2.PokMove(hostname = hostname))
                b = res.count
                if(b != noOfPokemons):
                    run(hostname)
                else:
                    print("closing the channel....")
                    print("Hurray all pokemons got captured!!!")
                    channel.close()
            else:
                print("Sorry you are already captured")
                channel.close()
                
        elif(hostname.startswith("Tra")):
            print("Trainer is moving")
            res = stub.TrainerMove(pb2.TrainMove(hostname = hostname))
            a = res.count
            if( a != noOfPokemons):
                run(hostname)
            else:
                print("closing the channel....")
                print("Hurray pokemons got captured!!!")
                channel.close()
            
def calculateDistance(pokwmonRow, pokemonColumn, trainerRow, trainerColumn):
    euc_dist = math.sqrt((pokwmonRow-trainerRow)*(pokwmonRow-trainerRow) + (pokemonColumn-trainerColumn)*(pokemonColumn-trainerColumn))
    return euc_dist

def searchOtherPlayer(hostname):
    row,column = searchPosition(hostname) 
    i = 0
    j = 0
    u1 = 0
    v1 = 0
    min_dist = 100.00
    for i in range(0,n):
        for j in range(0,n):
            if(matrix[i][j] != "🔷"):
                name = searchPlayer(i, j)
                if(name[0:5] != hostname[0:5]):
                    if(i != row and j != column):
                        if(calculateDistance(row,column,i,j) < min_dist):
                            min_dist = calculateDistance(row,column,i,j)
                            u1 = i
                            v1 = j
                else:
                    continue
    return u1, v1

def searchPosition(hostname):
    for key in initial_moves:
        if(key == hostname):
            row = initial_moves[key][0]
            column = initial_moves[key][1]
    return row, column

def searchPlayer(v1, v2):
    name = ""
    for key, (val1,val2) in initial_moves.items():
        if(val1 == v1 and val2 == v2):
            name = key
    return name

def moveUp(hostname,i,j):
    name=""
    i = i-1
    j = j
    if(i < 0):
       i=0
    if(matrix[i][j]!="🔷"):
        if(hostname.startswith("Tra")):
            name = searchPlayer(i,j)
            if(name.startswith("Tra")):
                i, j = moveSouthEast(hostname,i,j)
        elif(hostname.startswith("Pok")):
            i, j = moveSouthEast(hostname,i,j)
    return i, j 

def moveDown(hostname,i,j): 
    name = "" 
    i = i+1
    j = j
    if(i > n-1):
        i = n-1
    if(matrix[i][j]!="🔷"):
        if(hostname.startswith("Tra")):
            name = searchPlayer(i,j)
            if(name.startswith("Tra")):
                i, j = moveNorthWest(hostname,i,j)
        elif(hostname.startswith("Pok")):
            i, j = moveNorthWest(hostname,i,j)
    return i, j  

def moveRight(hostname,i,j):
    name =""
    i = i
    j = j+1
    if(j > n-1):
        j = n-1
    if(matrix[i][j]!="🔷"):
        if(hostname.startswith("Tra")):
            name = searchPlayer(i,j)
            if(name.startswith("Tra")):
                i, j = moveSouthWest(hostname,i,j)
        elif(hostname.startswith("Pok")):
            i, j = moveSouthWest(hostname,i,j)
    return i, j

def moveLeft(hostname,i,j):
    name=""
    i=i
    j=j-1
    if(j < 0):
        j = 0
    if(matrix[i][j]!="🔷"):
        if(hostname.startswith("Tra")):
            name = searchPlayer(i,j)
            if(name.startswith("Tra")):
                i, j = moveNorthEast(hostname,i,j)
        elif(hostname.startswith("Pok")):
            i, j = moveNorthEast(hostname,i,j)
    return i, j

def moveSouthEast(hostname,i,j):
    name =""
    i = i-1
    if(i < 0):
        i=0
    j = j+1
    if(j > n-1):
        j=n-1
    if(matrix[i][j]!="🔷"):
        if(hostname.startswith("Tra")):
            name = searchPlayer(i,j)
            if(name.startswith("Tra")):
                i, j = moveRight(hostname,i,j)
        if(hostname.startswith("Pok")):
            i, j = moveRight(hostname,i,j)
    return i, j

def moveSouthWest(hostname,i,j):
    name = ""
    i = i+1
    if(i > n-1):
        i=n-1
    j = j+1
    if(j > n-1):
        j=n-1
    if(matrix[i][j]!="🔷"):
        if(hostname.startswith("Tra")):
            name = searchPlayer(i,j)
            if(name.startswith("Tra")):
                i, j = moveDown(hostname,i,j)
        elif(hostname.startswith("Pok")):
            i, j = moveDown(hostname,i,j)
    return i, j

def moveNorthEast(hostname,i,j):
    name = ""
    i=i-1
    j=j-1
    if(i < 0):
        i=0
    if(j < 0):
        j=0
    if(matrix[i][j]!="🔷"):
        if(hostname.startswith("Tra")):
            name = searchPlayer(i,j)
            if(name.startswith("Tra")):
                i, j = moveUp(hostname,i,j)
        elif(hostname.startswith("Pok")):
            i, j = moveUp(hostname,i,j)
    return i, j

def moveNorthWest(hostname,i,j):
    name = ""
    i=i+1
    if(i > n-1):
        i=n-1
    j=j-1
    if(j < 0):
        j=0
    if(matrix[i][j]!="🔷"):
        if(hostname.startswith("Tra")):
            name = searchPlayer(i,j)
            if(name.startswith("Tra")):
                i, j = moveLeft(hostname,i,j)
        elif(hostname.startswith("Pok")):
            i, j = moveLeft(hostname,i,j)
    return i, j

def moveTrainer(hostname):
    global msg
    msg = ""
    global name
    name =""
    row, column = searchPosition(hostname)
    opprow, oppcol = searchOtherPlayer(hostname)

    if(row < opprow) and (column < oppcol):
        newrow, newcolumn = moveSouthWest(hostname, row, column)
        print('moving south west')
        if(newrow==opprow) and (newcolumn == oppcol):
            if(matrix[opprow][oppcol]!="🔷"):
                msg = "captured"
                name = searchPlayer(opprow, oppcol)
                if(name!=""):
                    initial_moves.pop(name)
        initial_moves[hostname] = newrow, newcolumn
        matrix[newrow][newcolumn] = matrix[row][column]
        matrix[row][column] = "🔷"
    elif(row < opprow) and (column > oppcol):
        newrow, newcolumn = moveNorthWest(hostname, row, column)
        if(newrow==opprow) and (newcolumn == oppcol):
            if(matrix[opprow][oppcol]!="🔷"):
                msg = "captured"
                name = searchPlayer(opprow, oppcol)
                if(name!=""):
                    initial_moves.pop(name)
        print('moving north west')
        initial_moves[hostname] = newrow, newcolumn
        matrix[newrow][newcolumn] = matrix[row][column]
        matrix[row][column] = "🔷"
    elif(row > opprow) and (column < oppcol):
        newrow, newcolumn = moveSouthEast(hostname, row, column)
        if(newrow==opprow) and (newcolumn == oppcol):
            if(matrix[opprow][oppcol]!="🔷"):
                msg = "captured"
                name = searchPlayer(opprow, oppcol)
                if(name!=""):
                    initial_moves.pop(name)
        print('moving south east')
        initial_moves[hostname] = newrow, newcolumn
        matrix[newrow][newcolumn] = matrix[row][column]
        matrix[row][column] = "🔷"
    elif(row > opprow) and (column > oppcol):
        newrow, newcolumn = moveNorthEast(hostname, row, column)
        if(newrow==opprow) and (newcolumn == oppcol):
            if(matrix[opprow][oppcol]!="🔷"):
                msg = "captured"
                name = searchPlayer(opprow, oppcol)
                if(name!=""):
                    initial_moves.pop(name)
        print('moving north east')
        initial_moves[hostname] = newrow, newcolumn
        matrix[newrow][newcolumn] = matrix[row][column]
        matrix[row][column] = "🔷"
    elif(row == opprow) and (column < oppcol):
        newrow, newcolumn = moveRight(hostname, row, column)
        if(newrow==opprow) and (newcolumn == oppcol):
            if(matrix[opprow][oppcol]!="🔷"):
                msg = "captured"
                name = searchPlayer(opprow, oppcol)
                if(name!=""):
                    initial_moves.pop(name)
        print('moving right')
        initial_moves[hostname] = newrow, newcolumn
        matrix[newrow][newcolumn] = matrix[row][column]
        matrix[row][column] = "🔷"
    elif(row == opprow) and (column > oppcol):
        newrow, newcolumn = moveLeft(hostname, row, column)
        if(newrow==opprow) and (newcolumn == oppcol):
            if(matrix[opprow][oppcol]!="🔷"):
                msg = "captured"
                name = searchPlayer(opprow, oppcol)
                if(name!=""):
                    initial_moves.pop(name)
        print('moving left')
        initial_moves[hostname] = newrow, newcolumn
        matrix[newrow][newcolumn] = matrix[row][column]
        matrix[row][column] = "🔷"
    elif(row > opprow) and (column == oppcol):
        newrow, newcolumn = moveDown(hostname, row, column)
        if(newrow==opprow) and (newcolumn == oppcol):
            if(matrix[opprow][oppcol]!="🔷"):
                msg = "captured"
                name = searchPlayer(opprow, oppcol)
                if(name!=""):
                    initial_moves.pop(name)
        print('moving down')
        initial_moves[hostname] = newrow, newcolumn
        matrix[newrow][newcolumn] = matrix[row][column]
        matrix[row][column] = "🔷"
    elif(row < opprow) and (column == oppcol):
        newrow, newcolumn = moveUp(hostname, row, column)
        if(newrow==opprow) and (newcolumn == oppcol):
            if(matrix[opprow][oppcol]!="🔷"):
                msg = "captured"
                name = searchPlayer(opprow, oppcol)
                if(name!=""):
                    initial_moves.pop(name)
        print('moving up')
        initial_moves[hostname] = newrow, newcolumn
        matrix[newrow][newcolumn] = matrix[row][column]
        matrix[row][column] = "🔷"
    elif(row == opprow) and (column == oppcol):
        newrow = row
        newcolumn = column
        msg = ""

    for row in matrix:
            spaciousMatrix="  ".join(map(str,row))
            print(spaciousMatrix)
    return msg
    
def movePokemon(hostname):
    global msg
    msg = ""
    if hostname in initial_moves.keys():
        row, column = searchPosition(hostname)
        name = searchPlayer(row, column)
        opprow, oppcol = searchOtherPlayer(hostname)
        if(row < opprow) and (column < oppcol):
            newrow, newcolumn = moveNorthEast(hostname, row, column)
            print('moving north east')
            initial_moves[hostname] = newrow, newcolumn
            matrix[newrow][newcolumn] = matrix[row][column]
            matrix[row][column] = "🔷"
        elif(row < opprow) and (column > oppcol):
            newrow, newcolumn = moveSouthEast(hostname, row, column)
            print('moving south east')
            initial_moves[hostname] = newrow, newcolumn
            matrix[newrow][newcolumn] = matrix[row][column]
            matrix[row][column] = "🔷"
        elif(row > opprow) and (column < oppcol):
            newrow, newcolumn = moveNorthWest(hostname, row, column)
            print('moving north west')
            initial_moves[hostname] = newrow, newcolumn
            matrix[newrow][newcolumn] = matrix[row][column]
            matrix[row][column] = "🔷"
        elif(row > opprow) and (column > oppcol):
            newrow, newcolumn = moveSouthWest(hostname, row, column)
            print('moving south west')
            initial_moves[hostname] = newrow, newcolumn
            matrix[newrow][newcolumn] = matrix[row][column]
            matrix[row][column] = "🔷"
        elif(row == opprow) and (column < oppcol):
            newrow, newcolumn = moveLeft(hostname, row, column)
            print('moving left')
            initial_moves[hostname] = newrow, newcolumn
            matrix[newrow][newcolumn] = matrix[row][column]
            matrix[row][column] = "🔷"
        elif(row == opprow) and (column > oppcol):
            newrow, newcolumn = moveRight(hostname, row, column)
            print('moving right')
            initial_moves[hostname] = newrow, newcolumn
            matrix[newrow][newcolumn] = matrix[row][column]
            matrix[row][column] = "🔷"
        elif(row > opprow) and (column == oppcol):
            newrow, newcolumn = moveUp(hostname, row, column)
            print('moving up')
            initial_moves[hostname] = newrow, newcolumn
            matrix[newrow][newcolumn] = matrix[row][column]
            matrix[row][column] = "🔷"
        elif(row < opprow) and (column == oppcol):
            newrow, newcolumn = moveDown(hostname, row, column)
            print('moving down')
            initial_moves[hostname] = newrow, newcolumn
            matrix[newrow][newcolumn] = matrix[row][column]
            matrix[row][column] = "🔷"
        elif(row == opprow) and (column == oppcol):
            msg = ""
        for row in matrix:
                spaciousMatrix="  ".join(map(str,row))
                print(spaciousMatrix)
        return msg
    else:
        msg = "captured"
    return msg

with open('contents.txt', 'r') as f:
    values = f.readlines()
noOfTrainers = int(values[0])
noOfPokemons = int(values[1])
n = int(values[2])
initial_moves={}

matrix = numpy.full([n, n], "🔷", dtype='object')

if __name__=='__main__':
    count = 0
    countPokemon = 0
    serve()