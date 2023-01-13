// Minimax

package main

import (
	"fmt"
	"math"
)

func minimax(currentDepth int, nodeIndex int, isMaxPlayer bool, scores []int, targetDepth int) int {
	// Check if the current depth equal to the target depth, if true return current score of current node
	if currentDepth == targetDepth {
		return scores[nodeIndex]
	}
	// If the current player is the max player, return max value between right and left children of the current node
	if isMaxPlayer {
		return max(minimax(currentDepth+1, nodeIndex*2, false, scores, targetDepth),
			minimax(currentDepth+1, nodeIndex*2+1, false, scores, targetDepth))
	} else {
		// If the current player is the min player, return min value between right and left children of the current node
		return min(minimax(currentDepth+1, nodeIndex*2, true, scores, targetDepth),
			minimax(currentDepth+1, nodeIndex*2+1, true, scores, targetDepth))
	}
}

// Helper function
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// Helper function
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// Run
func main() {
	// List of scores
	scores := []int{-1, 4, 2, 6, -3, -5, 0, 7}

	// Calculate max depth of the tree
	treeDepth := int(math.Log2(float64(len(scores))))

	fmt.Println("Best value : ", minimax(0, 0, true, scores, treeDepth))
}
