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
    def search(grid: Grid) -> Solution | NoSolution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points
            
        Returns:
            Solution: Solution found
        """
        node = Node("", grid.start, 0)

        # Verificamos si el nodo inicial no es la solución
        if node.state == grid.end:
            return Solution(node, explored={node.state: True})

        # Creo la frontera y el historial de nodos explorados
        frontier = StackFrontier() #LIFO
        frontier.add(node)
        explored = {}
        
        while True:
            # Si no quedan nodos por recorrer no hay solución
            if frontier.is_empty():
                return NoSolution(explored)
            
            current_node = frontier.remove() 
            if current_node.state in explored: 
                continue # Evita recorrer estados ya recorridos

            explored[current_node.state] = True
            neighbours = grid.get_neighbours(current_node.state)

            for action, new_state in neighbours.items():
                if new_state not in explored:
                    new_node = Node(
                        value=grid.get_node(new_state).value,
                        state=new_state,
                        parent=current_node,
                        action=action,
                        cost=current_node.cost + grid.get_cost(new_state)
                    )

                    # En caso de encontrar la solución
                    if new_state == grid.end:
                        return Solution(new_node, explored)

                    frontier.add(new_node)
