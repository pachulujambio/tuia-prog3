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
    def search(grid: Grid) -> Solution | NoSolution:
        
        start = grid.get_node(grid.start).value # Valor del nodo inicial

        node = Node(
            value=start, 
            state=grid.start, 
            cost=0,
            parent=None,
            action=None
        )

        # En caso de que comience en la solución retornamos la misma
        if node.state == grid.end:
            return Solution(node, reached={node.state: True})

        # Creamos la frontera y el el historial de estados para evitar ciclos
        frontier = QueueFrontier() #es FIFO 
        frontier.add(node)
        reached = {node.state: True}

        # Sigo recorriendo en caso de que haya nodos aún no visitados
        while not frontier.is_empty():
            current_node = frontier.remove() 

            # Buscamos los vecinos del primer nodo de la cola
            successors = grid.get_neighbours(current_node.state)

            # Verificamos si un vecino del nodo es la solución
            for action, new_state in successors.items():
                # Para evitar repetir una búsqueda verifica que no haya sido alcanzado previamente
                if new_state not in reached:
                    new_node = Node(
                        value=grid.get_node(new_state).value,
                        state=new_state,
                        parent=current_node,
                        action=action,
                        cost=current_node.cost + grid.get_cost(new_state)
                    )

                    # En caso que algún estado de los nodos vecinos sea la solución se retorna el mismo
                    if new_state == grid.end:
                        return Solution(new_node, reached)

                    reached[new_state] = True # Setea estado para evitarlo a futuro
                    frontier.add(new_node) # Evita ciclos

        # En caso de que no haya solución utilizo la clase NoSolution proporcionada
        return NoSolution(reached)