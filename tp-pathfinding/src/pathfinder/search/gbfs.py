from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node
from typing import Tuple, Callable

# Algoritmo GBFS de pseudocodigo a proyecto de prog 3
"""
def graph_gbfs(grid: Grid, heuristic: Callable[[tuple[int, int]], float]) -> Solution | NoSolution:
    node = Node(state=grid.start, parent=None, action=None, cost=0)
    frontier = PriorityQueueFrontier()
    frontier.add(node, priority=heuristic(node.state))
    explored = {node.state: node.cost}

    while True:
        if frontier.is_empty():
            return NoSolution(explored)

        current_node = frontier.remove()

        if current_node.state == grid.end:
            return Solution(current_node, explored)

        successors = grid.get_neighbours(current_node.state)

        for action, new_state in successors.items():
            new_cost = current_node.cost + grid.get_cost(new_state)

            if new_state not in explored or new_cost < explored[new_state]:
                child_node = Node(
                    state=new_state,
                    parent=current_node,
                    action=action,
                    cost=new_cost
                )
                explored[new_state] = new_cost
                frontier.add(child_node, priority=heuristic(new_state))
"""

def manhattan(state: Tuple[int, int], solution: Tuple[int, int]) -> int:
    return abs(state[0] - solution[0]) + abs(state[1] - solution[1])

class GreedyBestFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution | NoSolution:
        """Find path between two points in a grid using Greedy Best First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node(value="", state=grid.start, cost=0)

        # Verificamos que el cominzo no sea la solución
        if grid.start == grid.end:
            return Solution(node, explored={grid.start: 0})
        
        frontier = PriorityQueueFrontier()
        frontier.add(node, priority=manhattan(grid.start, grid.end))
        explored: dict[Tuple[int,int], int] = {grid.start: 0}
        
        # Buscamos siempre que haya una frontera
        while not frontier.is_empty():
            current_node = frontier.pop() # Retira por prioridad

            # Verificar si el nodo es solución
            if current_node.state == grid.end:
                return Solution(current_node, explored)

            # Verificamos cada nodo vecino 
            for action, nbr in grid.get_neighbours(current_node.state).items():
                new_cost = current_node.cost + grid.get_cost(nbr) 

                # En caso de ser un nuevo nodo o mejorar el costo se suma a la frontera para explorar posteriormente
                if nbr not in explored or new_cost < explored[nbr]:
                    new_node = Node(
                        value=grid.get_node(nbr).value,
                        state=nbr,
                        cost=new_cost,
                        parent=current_node,
                        action=action
                    )
                    explored[nbr] = new_cost
                    frontier.add(new_node, priority=manhattan(nbr, grid.end))

        # Retornar que no hay solución en caso de no tener mas frontera por recorrer
        return NoSolution(explored)
