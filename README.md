# cs5113fa22-project

## Development Schedule

 Architecture Description [10/26]
 -- Readme.md file - 10/26

 Protos and interface design complete [11/03]
  -- Protos - 10/29
  -- docker-compose.yml - 11/03

 First version logging [11/17]
 -- Server.py - 11/07
 -- Pokemon.py - 11/10
 -- Trainer.py - 11/15

 Submission [12/01]
 -- Working model - 11/30

 ## Emoji Chooser

 I am fixing the board size N x N to be 8 x 8.
 I am prompting the user to enter the number of pokemons(P) and trainers(T) and accordingly my ruamel program will pick these supplied data and generate the  docker-compose.yml file.
 I am giving a list of emojis to the user and they will choose through command line arguments.

 I am going to use:
 Emojis for Pokemon:
 🐶 Dog Face
 🐺 Wolf
 🦊 Foxemoji
 🦁 Lion

 Emojis for Trainer: 
 💁‍♀️ Woman Tipping Hand
 👶 Baby
 👀 Eyes
 👻 Ghost
 
 My proto file will contain the methods and rpc's that are needed to communicate with the server.
 Dockerfile will have configurations and it will run the python file that contains the code to generate the docker-compose.yml

 ##  Interfaces
 ------- Proto File --------
 ** pokemonou.proto is the proto buffer file that contains the rpc functions used to communicate with the server.
 
 It has following functions:
 1) Board -- input : Hostname and returns : InitialMoves. - used to check if pokemon exists or not, if exists it returns True else empty string
 2) TrainerMove -- input : TrainMove and returns : Message. this is used to just make the move
 3) PokemonMove -- this is used to just make the move
------ Dockerfile----------
DockerFile contains all the configurations that is a prerequisite to run docker which installs all the dependencies that are needed and run the python file that contains code to generate the docker-compose.yml file dynamically.
 
------ docker-compose.yml---------
 To generate the docker-compose.yml file, I run generatedockercompose.py file through DockerFile which takes input P(no. of Pokemons) and T(No. of Trainers) and generate the corresponding no. of clients in docker-compose.yml file. 
 Commands used:
  docker build . --- generates an image id
  docker run -it -v $(pwd):/usr/src/app <imageid> --- using the volume concept of docker so that it can generate docker-compose.yml
 
------ Testing -------
By using this command, python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. pokemonou.proto,
proto will generate 2 files, pokemonou_pb2_grpc.py and pokemonou_pb2.py which will contain the stubs that i will be implemnting on the pokemon and trainers which will send the input for Captured Moves and Board rpc functions and server will respond to them.

------ First version logging ------
Taking the trainer and pokemon emoji list through a text file and assigning random emojis to the pokemons and trainers. When user gives board size, number of pokemons and number of trainers in input it gets saved in the contents.txt file and we use that file in the server.py to create the board using numpy.empty() method. 

To Note: For now initializing the array elements as none, later as the functionality develops, will update those. 
 
 For now, i am using the same docker file for server, trainer as well as pokemon. Therefore, seeing the same output for all.


![first_version_gif (1)](https://user-images.githubusercontent.com/114453254/202829395-1a5da473-aa91-4012-904a-ee58be2425c8.gif)



