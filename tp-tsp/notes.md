# Notas para resolver el enunciado

## Tabu
### PseudoCodigo
1 function BÚSQUEDA-TABÚ(problema) return estado
2 actual ← problema.estado-inicial
3 mejor ← actual
4 tabu ← inicialmente vacía
5 while no se cumpla el criterio de parada do
6 accion ← MAX-ACCION(problema, actual, tabu)
7 sucesor ← problema.resultado(actual, accion)
8 if problema.f(mejor) < problema.f(sucesor) then mejor ← sucesor
9 actualizar la lista tabú
10 actual ← sucesor
11 return mejor

### Traducción a python y ejercicios


## HillClimbing
### Pseudocodigo
1 function MAX-ACCION(problema, s: estado) return accion
2 sucesores ← {a: problema.f(problema.resultado(s,a))
for a in problema.acciones(s)}
3 return max(sucesores, key=sucesores.get)

function ASCENSIÓN-COLINAS(problema) return estado
2 actual ← problema.estado-inicial
3 do
4 accion ← MAX-ACCION(problema, actual)
5 sucesor ← problema.resultado(actual, accion)
6 if (problema.f(sucesor) ≤ problema.f(actual)) then return actual
7 actual ← sucesor

## HillClimbingReset
Adaptación del código

function HILL-CLIMBING-RESET(problema, max_reinicios) return estado
    mejor ← problema.estado_inicial
    mejor_val ← problema.f(mejor)
    for i desde 1 hasta max_reinicios hacer
        if i == 1 entonces
            actual ← problema.estado_inicial
        sino
            actual ← problema.random_reset()
        fin si
        actual_val ← problema.f(actual)
        repetir
            accion ← MAX-ACCION(problema, actual)
            sucesor ← problema.resultado(actual, accion)
            sucesor_val ← problema.f(sucesor)
            si sucesor_val ≤ actual_val entonces
                salir del bucle
            fin si
            actual ← sucesor
            actual_val ← sucesor_val
        hasta falso
        si actual_val > mejor_val entonces
            mejor ← actual
            mejor_val ← actual_val
        fin si
    fin para
    return mejor