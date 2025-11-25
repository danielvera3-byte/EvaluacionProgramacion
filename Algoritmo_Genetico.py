import numpy
import pygad
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import datasets

# Cargamos los datos de las flores Iris (un ejemplo clásico)
iris = datasets.load_iris()
X, y = iris.data, iris.target

# Separamos una parte para entrenar y otra para probar
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

def fitness_func(ga_instance, solution, solution_idx):
    """
    Esta función es el 'juez'. El algoritmo genético prueba un número (solution[0])
    y aquí vemos qué tan bueno es ese número para configurar nuestro modelo.
    """
    k = max(1, int(solution[0])) # El número de vecinos debe ser al menos 1
    
    # Creamos el modelo con ese valor K
    modelo = KNeighborsClassifier(n_neighbors=k)
    modelo.fit(X_train, y_train)
    
    # Probamos qué tan bien predice
    precision = modelo.score(X_test, y_test)
    
    return precision

# Configuramos el Algoritmo Genético
ga_instance = pygad.GA(
    num_generations=20,         # Cuantas generaciones evolucionará
    num_parents_mating=4,       # Cuantos padres se cruzan
    fitness_func=fitness_func,  # La función juez de arriba
    sol_per_pop=8,              # Cuantos individuos por población
    num_genes=1,                # Solo buscamos 1 número (el valor K)
    gene_space=[range(1, 30)],  # El valor K puede ser de 1 a 30
    parent_selection_type="sss",
    crossover_type="single_point",
    mutation_type="random",
    mutation_percent_genes=10
)

print("Ejecutando Algoritmo Genético para optimizar modelo...")
ga_instance.run()

# Vemos cuál fue el ganador
solution, solution_fitness, solution_idx = ga_instance.best_solution()
mejor_k = int(solution[0])

print(f"\n¡Listo! El Algoritmo Genético encontró que el mejor K es: {mejor_k}")
print(f"Con una precisión de: {solution_fitness}")