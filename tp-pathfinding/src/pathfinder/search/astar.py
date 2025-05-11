from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node
from .gbfs import manhattan
from typing import Callable, Tuple

# Algoritmo A* adaptado al proyecto actual
"""
def graph_astar(grid: Grid, heuristic: Callable[[tuple[int, int]], float]) -> Solution | NoSolution:
    node = Node(state=grid.start, parent=None, action=None, cost=0)

    frontier = PriorityQueueFrontier()
    frontier.add(node, priority=node.cost + heuristic(node.state))

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
                priority = child_node.cost + heuristic(new_state)
                frontier.add(child_node, priority=priority)
"""

# Reutilice el código de GBFS en gran parte de la clase, salvo en el agregado a la frontera (en la prioridad)
class AStarSearch:
    @staticmethod
    def search(grid: Grid) -> Solution | NoSolution:
        """Find path between two points in a grid using A* Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # Verificamos que el cominzo no sea la solución
        if grid.start == grid.end:
            return Solution(node, explored={grid.start: 0})
        
        frontier = PriorityQueueFrontier()
        frontier.add(node, priority=0 + manhattan(grid.start, grid.end))
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
                    frontier.add(new_node, priority=new_cost + manhattan(nbr, grid.end))

        return NoSolution(explored)
