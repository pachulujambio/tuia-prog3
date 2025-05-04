from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

# Algoritmo en pseudo-codigo de teoria con algunos cambios teniendo en cuenta el proyecto actual
"""
function graph-bfs(grid) return solucion o fallo
    node = Node(grid.start, None, None, 0)
    if node.state == grid.end then return Solution(node, reached)
    frontier = QueueFrontier()
    frontier.add(node)
    reached = {}; reached[node.state] = True
    do
        if frontier.is_empty() then return fallo
        n = frontier.remove()
        successors = grid.get_neighbours(n.state)
        for all action in successors do
            new_state = successors[action]
            if new_state not in reached then
                new_node = Node(new_state, n, action, n.cost + grid.get_cost(new_state))
                if new_state == grid.end then return Solution(new_node, reached)
                reached[new_state] = True
                frontier.add(new_node)
"""

class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

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
