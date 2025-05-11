from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


# Algoritmo UCS adaptado al proyecto actual
"""
def graph_ucs(grid: Grid) -> Solution | NoSolution:
    node = Node(state=grid.start, parent=None, action=None, cost=0)
    frontier = PriorityQueueFrontier()
    frontier.add(node, node.cost)
    explored = {node.state: node.cost}

    while True:
        if frontier.is_empty():
            return NoSolution(explored)

        current_node = frontier.remove()

        if current_node.state == grid.end:
            return Solution(current_node, explored)

        successors = grid.get_neighbours(current_node.state)

        for action, new_state in neighbours.items():
            new_cost = current_node.cost + grid.get_cost(new_state)

            if new_state not in explored or new_cost < explored[new_state]:
                child_node = Node(
                    state=new_state,
                    parent=current_node,
                    action=action,
                    cost=new_cost
                )
                explored[new_state] = new_cost
                frontier.add(child_node, new_cost)
"""

class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution | NoSolution:
        """Find path between two points in a grid using Uniform Cost Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # Crear frontera e historial, use una lista de prioridades porque así lo decía la teoria
        # Por eso cambie la clase del objeto frontera
        frontier = PriorityQueueFrontier() 
        frontier.add(node, node.cost)
        explored = {node.state: node.cost}

        while not frontier.is_empty():
            current_node = frontier.pop() # Nodo de menor prioridad
            
            # Verificamos si el nodo es la solución
            if current_node.state == grid.end:
                return Solution(current_node, explored)

            # Bbtenemos los nodos vecinos
            successors = grid.get_neighbours(current_node.state)

            # Por cada vecino se calcula si el costo sería menor en el mismo,
            # en caso de serlo se agrega a la frontera porque puede ser una solución,
            # O si aún no fue explorado
            for action, new_state in successors.items():
                new_cost = current_node.cost + grid.get_cost(new_state)

                # Ignorar instancias antiguas
                if current_node.cost > explored[current_node.state]:
                    continue

                # se compara el costo mencionado previamente
                if new_state not in explored or new_cost < explored[new_state]:
                    new_node = Node(
                        value=grid.get_node(new_state).value,
                        state=new_state,
                        parent=current_node,
                        action=action,
                        cost=current_node.cost + grid.get_cost(new_state)
                    )
                    # Asignación mencionada previamente
                    explored[new_state] = new_cost
                    frontier.add(new_node, new_cost)

        return NoSolution(explored)
