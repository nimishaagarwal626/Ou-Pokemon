# cs5113fa22-project

## Development Schedule

 Architecture Description [10/26]

 Protos and interface design complete [11/03]
  -- Protos - 10/29
  -- docker-compose.yml - 11/03

 First version logging [11/17]

 Submission [12/01]

 ## Emoji Chooser

 I am fixing the board size N x N to be 8 x 8.
 I am prompting the user to enter the number of pokemons and trainers and accordingly my ruamel program will pick these supplied data and generate the  docker-compose.yml file.
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

 ##  Interfaces
 pokemon.proto is the proto buffer file that contains the rpc functions used to communicate with the server.s
 It has 3 functions:
 1) Captured -- which takes input as pokemonName and returns the feedback saying "pokemonName" is captured.
 2) Moves -- which take input as stream of player and return stream Feedback that says where the move is i.e., the row and column specification.
 3) Board -- which takes BoardConfig as input and returns BoardConfig.

 To generate the docker-compose.yml file, I run generatedockercompose.py file through DockerFile.
 Commands used:
  docker build .
  docker run -it <imageid>



