"""Este modulo define la clase LocalSearch.

LocalSearch representa un algoritmo de busqueda local general.

Las subclases que se encuentran en este modulo son:

* HillClimbing: algoritmo de ascension de colinas. Se mueve al sucesor con
mejor valor objetivo. Ya viene implementado.

* HillClimbingReset: algoritmo de ascension de colinas de reinicio aleatorio.
No viene implementado, se debe completar.

* Tabu: algoritmo de busqueda tabu.
No viene implementado, se debe completar.
"""


from __future__ import annotations
from time import time
from problem import OptProblem


class LocalSearch:
    """Clase que representa un algoritmo de busqueda local general."""

    def __init__(self) -> None:
        """Construye una instancia de la clase."""
        self.niters = 0  # Numero de iteraciones totales
        self.time = 0  # Tiempo de ejecucion
        self.tour = []  # Solucion, inicialmente vacia
        self.value = None  # Valor objetivo de la solucion

    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion."""
        self.tour = problem.init
        self.value = problem.obj_val(problem.init)


class HillClimbing(LocalSearch):
    """Clase que representa un algoritmo de ascension de colinas.

    En cada iteracion se mueve al estado sucesor con mejor valor objetivo.
    El criterio de parada es alcanzar un optimo local.
    """

    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion con ascension de colinas.

        Argumentos:
        ==========
        problem: OptProblem
            un problema de optimizacion
        """
        # Inicio del reloj
        start = time()

        # Arrancamos del estado inicial
        actual = problem.init
        value = problem.obj_val(problem.init)

        while True:

            # Buscamos la acción que genera el sucesor con mayor valor objetivo
            act, succ_val = problem.max_action(actual)

            # Retornar si estamos en un maximo local:
            # el valor objetivo del sucesor es menor o igual al del estado actual
            if succ_val <= value:

                self.tour = actual
                self.value = value
                end = time()
                self.time = end-start
                return

            # Sino, nos movemos al sucesor
            actual = problem.result(actual, act)
            value = succ_val
            self.niters += 1


class HillClimbingReset(LocalSearch):
    """Algoritmo de ascension de colinas con reinicio aleatorio."""

    def solve(self, problem: OptProblem) -> None:
        """
        Ejecuta varias ascensiones de colina, reiniciando aleatoriamente
        para escapar de óptimos locales, y selecciona la mejor solución.
        """
        start = time()
        original_init = problem.init # Guardar estado inicial original
        best = None
        best_val = None
        iteraciones_totales = 0
        max_reinicios = 15

        # Repetir ascensión de colinas max_reinicios veces (hardcodeado porque no lo llama en main)
        for i in range(1, max_reinicios + 1):
            # Selección del estado de inicio: original o reinicio aleatorio
            if i == 1:
                problem.init = original_init
            else:
                problem.init = problem.random_reset()

            # Reutilizo HillClimbing
            hc = HillClimbing()
            hc.solve(problem)

            # Acumular iteraciones
            iteraciones_totales += hc.niters

            # Actualizar mejor solución global
            if best_val is None or hc.value > best_val:
                best = hc.tour
                best_val = hc.value

        # Restaurar estado inicial y guardar resultados
        problem.init = original_init
        self.tour = best
        self.value = best_val
        self.niters = iteraciones_totales
        self.time = time() - start


class Tabu(LocalSearch):
    """Algoritmo de busqueda tabu."""

    # COMPLETAR
