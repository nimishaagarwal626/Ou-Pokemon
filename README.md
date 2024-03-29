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
 2) TrainerMove -- input : TrainMove and returns : Message. this is used to just make the move and capture the pokemon
 3) PokemonMove -- input : PokMove and returns : Message. this is used to just make the move away from the trainer

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

------ Final Submission -----------
My code base contains:
Code:
  generatedockercompose.py
  node.py
  Dockerfile
  docker-compose.yml
  pokemons_emojis.txt
  trainers_emojis.txt
  requirements.txt
  contents.txt
COLLABORATORS
README.md

To test the complete working module:
Make sure Dockerfile has generatedockercompose.yml in CMD 
I first run docker build. - It generates and image id
Then, I run docker run -it -v $(pwd):/usr/src/app <imageid> where image id is the one generated by the above command. - This asks to enter the number of pokemon and trainers as well as the board size and store in contents.txt file. Based on i/p provided, it generates docker-compose.yml file
Then make sure dockerfile has node.py in CMD
Then run docker-compose up --build --remove-orphans

As the board was created and pokemons were placed on the board in previous versions. Here, I am trying to move the pokemons and trainers on the board using the following method:
For Pokemon :::
When the Pokemon contaires starts, it requests Board at every step from the server to check the trainers positions. Now, it tries to see where is the nearest trainer present using the calculate distance and searchOtherPlayer methods. When it finds the nearest trainer, that pokemon tries to move away from Trainer.
It uses 8 directions to move: Up, Down, Right, Left, SouthEast, SouthWest, NorthEast, NorthWest. To move it in different directions, i have used conditions to check if the row and column of pokemon is < or > or =  the trainers and based on it, Pokemons move is decided.
For Trainer :::
When the Trainer containers starts, it requests Board at every step from the server to check the pokemons positions. Now, it tries to see where is the nearest pokemon present using the calculate distance and searchOtherPlayer methods. When it finds the nearest pokemon, that trainer tries to move towards the nearest Pokemon. Trainer also uses 8 directions to move: Up, Down, Right, Left, SouthEast, SouthWest, NorthEast, NorthWest. To move it in different directions, i have used conditions to check if the row and column of trainer is < or > or =  the pokemons and based on it, Trainers move is decided.
At every step Trainer checks if its position becomes equal to the Pkemons positions it send a message to the server saying message is captured.

Handling of Pokemon not making a move if it is captured :::
I am maintaining a dictionary on the server for keeping track of positions of trainers and pokemons. Whenever a pokemon is captured, I pop out that pokemon from the list. And when pokemon requests the board it checks if that pokemon exists in the dictionary or not and if it exists it return true and then only the Pokemon is allowed to make a move otherwise it closes its channel.

To handle concurrency i.e. if trainer is making a move it should complete the move, I am making use of locks in the server side while calling the movePokemon and moveTrainer Methods.
To handle the execution that all channels should be closed after all the pokemons are captured, I am making use of 2 count variables, one for pokemon and another one for trainer, Trainer increaments the count whenever a pokemon is captured and Pokemon increaments the count whenever it is captured and still coming for the execution it increments the count.
And i made use of recursive call of clients based on if my count is equal to the number of pokemons, it closes the channel, otherwise call the run(hostname){this method is where the client is} method again.

DS Problems faced:::
Issue#1 - Multithreading concurrency issue => Resolution - Locks
Issue#2 - Scalability => Resolution - generating docker-compose.yml dynamically to accomadate any number of trainers, pokemon as well as the board size
Issue#3 - Message Passing => Resolution - Use of RPCs iinstead of Send and Receive

Gif for code Run::

![Screen_Recording_2022-12-14_at_2_24_51_AM_AdobeExpress (2)](https://user-images.githubusercontent.com/114453254/207578064-1f82b6fa-da17-44df-8d00-7d26e5d7eb13.gif)

