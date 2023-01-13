# Minimax

import math

def minimax (currentDepth, nodeIndex, isMaxPlayer, scores, targetDepth):

    # Check if the current depth equal to the target depth, if true return current score of current node
    if (currentDepth == targetDepth):
        return scores[nodeIndex]
    
    # If the current player is the max player, return max value between right and left children of the current node
    if (isMaxPlayer):
        return max (minimax (currentDepth + 1, nodeIndex * 2, False, scores, targetDepth),
                    minimax(currentDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth))
    
    # If the current player is the min player, return min value between right and left children of the current node
    else :
        return min (minimax (currentDepth + 1, nodeIndex * 2, True, scores, targetDepth),
                    minimax(currentDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth))

# List of scores
scores = [-1, 4, 2, 6, -3, -5, 0, 7]

# Calculate max depth of the tree
treeDepth = math.log(len(scores), 2)

print("Best value : ", end = "")
print(minimax(0,0,True, scores, treeDepth))