from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

# Algoritmo DFS adaptado al proyecto actual
"""
function graph-dfs(grid) return solucion o fallo
    node = Node(grid.start, None, None, 0)
    if node.state == grid.end then return Solution(node, reached)
    frontier = StackFrontier()
    frontier.add(node)
    expanded = set()
    do
        if frontier.is_empty() then return fallo
        n = frontier.remove()
        if n.state in expanded then continue
        expanded.add(n.state)
        successors = grid.get_neighbours(n.state)
        for all action in successors do
            new_state = successors[action]
            if new_state not in expanded then
                new_node = Node(new_state, n, action, n.cost + grid.get_cost(new_state))
                if new_state == grid.end then return Solution(new_node, expanded)
                frontier.add(new_node)
"""

class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points
            
        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # Initialize the explored dictionary to be empty
        explored = {} 
        
        # Add the node to the explored dictionary
        explored[node.state] = True
        
        return NoSolution(explored)
