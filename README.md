# Red-Blue-Nim

Developed a computer human game where initally there are fixed number of red and blue balls and each player gets to choose a ball on their turn. The player wins when there is no ball present to remove on a their turn. 

Command to Run Code
------------------------------------------------------------------------------------------------------------
Below are the possible commands which can be given to run the following code:
1. python3 red_blue_nim.py <red_ball_count> <blue_ball_count> <player> <depth> 
2. python3 red_blue_nim.py <red_ball_count> <blue_ball_count> <player> 
3. python3 red_blue_nim.py <red_ball_count> <blue_ball_count>

example1: python3 red_blue_nim.py 2 3 human
example2: python3 red_blue_nim.py 2 3 computer
example3: python3 red_blue_nim.py 2 3 
example4: python3 red_blue_nim.py 2 3 human 3

exmaple1 indicates that the human will be the first player to play the game containing 2 red balls and 3 blue balls.
exmaple2 indicates that the computer will be the first player to play the game containing 2 red balls and 3 blue balls.
example3 indicates that by default computer will be the first player to play the game containing 2 red balls and 3 blue balls.
example4 indicates that the human player will start the game with 2 red and 3 blue balls and in the computer player turn it will implement depth limited minmax alpha beta pruning search.

Code Structuring
------------------------------------------------------------------------------------------------------------
1. Whole code is structued in a single file.
2. The program starts from the "main" function and takes takes the arguments and calls "redBlueNim" function if depth is not provided and "redBlueNimDepth" function if depth is given.
3. In the "redBlueNim" or "redBlueNimDepth" functions it check whose is the player and redirects to its functions as specified below:
    - If its the computer turn then it directs to one of the below:
        * redBlueNimComputerDepth (if depth is given, function call takes place in "redBlueNimDepth" function)
        * redBlueNimComputer (if depth is not given, function call takes place in "redBlueNimDepth" function)
    - If its the human turn then it directs to one of the below:
        * redBlueNimHumanDepth (if depth is given, function call takes place in "redBlueNimDepth" function)
        * redBlueNimHuman (if depth is not given, function call takes place in "redBlueNimDepth" function)
4. The main functionality of the redBlueNimHuman or redBlueNimHumanDepth is:
    - Firstly, it starts with the human turn by prompting a question to enter their move i.e., to pick red or blue ball.
    - The user can type red or blue depending on the color ball he wants to select.
    - After the human turn we check whether any of the pile(red or blue) has zero balls. If there is an zero ball in either of the color balls it indicates that the computer has won the game and pops the score in the terminal using eval function (2*red_balls_remaining+3*blue_balls_remaining) present in checkWinner and calculateFinalCost functions.
    - If the checkWinner function returns false it means that the game has not ended and its the computer's turn.
    - In the computer's turn we calculate the move using the MinMax alpha beta pruning and take the action move produced in it as the next move.
    - After the computer turn we check again whether any of the pile(red or blue) has zero balls. If there is an zero ball in either of the color balls it indicates that the human has won the game and pops the score in the terminal using eval function (2*red_balls_remaining+3*blue_ball_remaining) present in checkWinner and calculateFinalCost functions.
5. "TerminalState" function checks whether the either of the piles red or blue has zero balls in it, to calculate the utility cost of it if they are zero depending on whether its a max state or a min state in MinMax alpha beta pruning (when depth not specified)
6. "calTerminalStateValDepth" function checks whether either of the piles red or blue has zero balls in it or if the tree has reached the required depth and calulates the utility value depending on the eval function provided.
