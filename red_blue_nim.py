import sys

# node class is created to stored the red ball count and blue ball count along with winFlag.
# winFlag is used to state whether the state winning state or not.
class node():
    def __init__(self, redBallCount, blueBallCount, winFlag):
        self.redBallCount = redBallCount
        self.blueBallCount = blueBallCount
        self.winFlag = winFlag

# Function checks whether redBallCount or blueBallCount is zero or not and modifies the winFlag accordingly and prints the value winner name along with their points.
def checkWinner(player, rootNode):
    if int(rootNode.redBallCount == 0) or int(rootNode.blueBallCount) == 0:
        cost = calculateFinalCost(rootNode.redBallCount, rootNode.blueBallCount)
        print(player,"won by ", cost , " points")
        rootNode.winFlag = True
        return rootNode

# Calculate the final score for the winner
def calculateFinalCost(red_ball_count, blue_ball_count):
    return 2*int(red_ball_count) + 3*int(blue_ball_count)

# Checks whether its the terminal/ utility state or not in computer's turn for MinMax alpha beta pruning tree
def TerminalState(rootNode):
    if int(rootNode.redBallCount) == 0 or int(rootNode.blueBallCount) == 0:
        return True
    return False

# Calulcates the utility value for the terminal state
def calTerminalStateVal(rootNode, val):
    if val == "max":
        return (int(rootNode.redBallCount)*2 + int(rootNode.blueBallCount)*3, rootNode)
    else: 
        res = int(rootNode.redBallCount)*2 + int(rootNode.blueBallCount)*3
        res = -1 * res
        return (res, rootNode)

# Generates successors for a node by removing a red ball and making it the left child and then removing the blue ball and making it the right child.
def createSuccessors(rootNode):
    nodes = []
    new_red_ball = int(rootNode.redBallCount) -1
    new_blue_ball = int(rootNode.blueBallCount)-1
    nodes.append(node(new_red_ball, rootNode.blueBallCount, "false"))
    nodes.append(node(rootNode.redBallCount, new_blue_ball, "false"))
    return nodes

# Minvalue function for the MinMax alpha beta tree
def MinValue(rootNode, alpha, beta):
    if TerminalState(rootNode):
        res = calTerminalStateVal(rootNode, "min")
        return res
    v = float('inf')
    state = rootNode
    for s in createSuccessors(rootNode):
        maxVal, stateVal = MaxValue(s, alpha, beta)
        v = min(v, maxVal)
        if v == maxVal:
            state = s
        if v<=alpha:
            return (v, state)
        beta = max(beta, v)
    return (v, state)

# Maxvalue function for the MinMax alpha beta tree
def MaxValue(rootNode, alpha, beta):
    if TerminalState(rootNode):
        return calTerminalStateVal(rootNode, "max")
    v = float('-inf')
    state = rootNode
    for s in createSuccessors(rootNode):
        minVal, stateVal = MinValue(s, alpha, beta)
        v = max(v, minVal)
        if v == minVal:
            state = s
        if v>=beta:
            # state = s
            return (v, state)
        alpha = max(alpha, v)
    return (v, state)

# calling the MinMax function in this if its the computer turn
def computerTurnValue(rootNode):
    v, state = MaxValue(rootNode, float('-inf'), float('inf'))
    print("Computer turn after picking balls leaves with red = ", state.redBallCount, "blue = ",state.blueBallCount)
    return state

# function for human turn to produce a question with the current state of balls remaining.
def humanTurnValue(rootNode):
    print("Number of Red Balls present: ", rootNode.redBallCount)
    print("Number of Blue Balls present: ", rootNode.blueBallCount)
    print("Pick a Ball(Red or Blue): ")
    humanResponse = input()
    if int(rootNode.redBallCount) == 0 or int(rootNode.blueBallCount) == 0:
        return node(rootNode.redBallCount, rootNode.blueBallCount, "true")
    if humanResponse.lower() == "red":
        redBallCount = int(rootNode.redBallCount) - 1
        return node(redBallCount, rootNode.blueBallCount, rootNode.winFlag)
    elif humanResponse.lower() == "blue":
        blueBallCount = int(rootNode.blueBallCount) - 1
        return node(rootNode.redBallCount, blueBallCount, rootNode.winFlag)
    else:
        print("Invalid pick please provide the answer again as Red or Blue to pick a pile")
        humanTurnValue(rootNode)

# Function which runs if the computer is the first player in the command line
def redBlueNimComputer(rootNode):
    while True:
        rootNode = computerTurnValue(rootNode)
        if checkWinner("Human", rootNode):
            return
        rootNode = humanTurnValue(rootNode)
        if checkWinner("Computer", rootNode):
            return

# Function which runs if the human is the first player in the command line  
def redBlueNimHuman(rootNode):
    while True:
        rootNode = humanTurnValue(rootNode)
        if checkWinner("Computer", rootNode):
            break
        rootNode = computerTurnValue(rootNode)
        if checkWinner("Human", rootNode):
            break
    return

# Determining which function to call depending on the player given in command line args
def redBlueNim(red_balls_count, blue_balls_count, player):
    rootNode = node(red_balls_count, blue_balls_count, "false")
    if player.lower() == "computer":
        redBlueNimComputer(rootNode)
    else:
        redBlueNimHuman(rootNode)

# extra credit depth limited min max alpha beta pruning

# calculating the utility value for the node when depth is specified
def calTerminalStateValDepth(rootNode, val):
    if val == "max":
        return (int(rootNode.redBallCount)*1 + int(rootNode.blueBallCount)*2, rootNode)
    else: 
        res = int(rootNode.redBallCount)*1 + int(rootNode.blueBallCount)*2
        res = -1 * res
        return (res, rootNode)

# Minvalue function in the MinMax alpha beta pruning for computer's turn along with depth
def MinValueDepth(rootNode, alpha, beta, depth):
    if int(depth) == 0 or TerminalState(rootNode):
        res = calTerminalStateValDepth(rootNode, "min")
        return res
    v = float('inf')
    state = rootNode
    for s in createSuccessors(rootNode):
        maxVal, stateVal = MaxValueDepth(s, alpha, beta, int(depth)-1)
        v = min(v, maxVal)
        if v == maxVal:
            state = s
        if v<=alpha:
            return (v, state)
        beta = max(beta, v)
    return (v, state)

# Maxvalue function in the MinMax alpha beta pruning for computer's turn along with depth
def MaxValueDepth(rootNode, alpha, beta, depth):
    if int(depth) == 0 or TerminalState(rootNode):
        return calTerminalStateValDepth(rootNode, "max")
    v = float('-inf')
    state = rootNode
    for s in createSuccessors(rootNode):
        minVal, stateVal = MinValueDepth(s, alpha, beta, int(depth) - 1)
        v = max(v, minVal)
        if v == minVal:
            state = s
        if v>=beta:
            return (v, state)
        alpha = max(alpha, v)
    return (v, state)

# calling the MinMax function in this if its the computer turn when depth is specified
def computerTurnValueDepth(rootNode, depth):
    v, state = MaxValueDepth(rootNode, float('-inf'), float('inf'), depth)
    print("Computer turn after picking balls leaves with red = ", state.redBallCount, "blue = ",state.blueBallCount)
    return state

# Function which runs if the computer is the first player in the command line when depth is specified
def redBlueNimComputerDepth(rootNode, depth):
    while True:
        rootNode = computerTurnValueDepth(rootNode, depth)
        if checkWinner("Human", rootNode):
            return
        rootNode = humanTurnValue(rootNode)
        if checkWinner("Computer", rootNode):
            return
        
# Function which runs if the human is the first player in the command line when depth is specified
def redBlueNimHumanDepth(rootNode, depth):
    while True:
        rootNode = humanTurnValue(rootNode)
        if checkWinner("Computer", rootNode):
            break
        rootNode = computerTurnValueDepth(rootNode, depth)
        if checkWinner("Human", rootNode):
            break
    return

# Determining which function to call depending on the player given in command line args when depth is specified
def redBlueNimDepth(red_balls_count, blue_balls_count, player, depth):
    rootNode = node(red_balls_count, blue_balls_count, "false")
    if player.lower() == "computer":
        redBlueNimComputerDepth(rootNode, depth)
    else:
        redBlueNimHumanDepth(rootNode, depth)

# main code where the program starts
def main(args):
    len_of_arguments = len(args)
    if len_of_arguments <2:
        print("Please enter the required red and blue ball count to start the game")
    if len_of_arguments == 2:
        redBlueNim(args[0], args[1], "computer")
    if len_of_arguments == 3:
        redBlueNim(args[0], args[1], args[2])
    if len_of_arguments == 4:
        redBlueNimDepth(args[0], args[1], args[2], args[3])
        # print("inside extra credit part!!!!")

main(sys.argv[1:])