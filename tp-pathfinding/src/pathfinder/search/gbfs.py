from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

# Algoritmo GBFS de pseudocodigo a proyecto de prog 3
"""
def graph_gbfs(grid: Grid, heuristic: Callable[[tuple[int, int]], float]) -> Solution | NoSolution:
    node = Node(state=grid.start, parent=None, action=None, cost=0)
    frontier = PriorityQueueFrontier()
    frontier.add(node, priority=heuristic(node.state))
    reached = {node.state: node.cost}

    while True:
        if frontier.is_empty():
            return NoSolution(reached)

        current_node = frontier.remove()

        if current_node.state == grid.end:
            return Solution(current_node, reached)

        successors = grid.get_neighbours(current_node.state)

        for action, new_state in successors.items():
            new_cost = current_node.cost + grid.get_cost(new_state)

            if new_state not in reached or new_cost < reached[new_state]:
                child_node = Node(
                    state=new_state,
                    parent=current_node,
                    action=action,
                    cost=new_cost
                )
                reached[new_state] = new_cost
                frontier.add(child_node, priority=heuristic(new_state))
"""

class GreedyBestFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Greedy Best First Search

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
