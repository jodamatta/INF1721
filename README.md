# analise_de_algoritmos
## INF1721 - Introduction to algorithms course at PUC-Rio

### Summary
This course is focused on introducing the students to the world of algorithms. We start up by learning to identify the complexity of the algorithm by its asymptotic behaviour, then we study recursion trees and graphs, and in the end we study the three main algorithm design frameworks: greedy, divide and conquer and dynamic programming.

### T1 - Linear time selection
The first project of the course was to develop a Linear time Selection algorithm, and we using the Median of Medians to find this solution. 

### T2 - Space state graph
For the second project, we we worked a game that can be played on a 3x3 board. Each node of the graph should be a possible state of the board, and the nodes have edges connecting them if it is possible to go from one state to another in a single move.
The first part was to code a function that creates the graph with all the possible states of the board and correctly link them by the edges. The second part was to implement a BFS algorithm to find the amount of connected components in the graph. The third and final part was to find the board layout that took the longest amount of moves (or the longest shortest path) to reach a boar state given by the professor.

### T3 - 10-Knapsack problem
In the last project of the course, we had to develop a dynamic programming algorithm to solve the Knapsack problem with a twist: now, we could add up to 10 elements of the same item to the backpack. The first part was to develop the recurence equation for the OPT function, and the second part was to implement the algorithm that fills up the memoization table with the OPT values.
