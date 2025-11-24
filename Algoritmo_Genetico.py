import numpy
import pygad
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import datasets

# --- DOCUMENTACIÓN DEL ALGORITMO ---
# Este script cumple con el objetivo de ejecutar, comprender y explicar un algoritmo genético.
# Se utiliza la librería PyGAD para optimizar los hiperparámetros (en este caso, 'n_neighbors')
# de un modelo KNeighborsClassifier de la librería scikit-learn.

# 1. Cargar datos de scikit-learn (Dataset Iris)
iris = datasets.load_iris()
X, y = iris.data, iris.target

# 2. Dividir datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

def fitness_func(ga_instance, solution, solution_idx):
    """
    Función de Aptitud (Fitness Function).
    El Algoritmo Genético usa esta función para evaluar qué tan buena es una solución.
    
    Aquí, 'solution[0]' es el número de vecinos (K) que el algoritmo propone.
    Entrenamos el modelo con ese K y devolvemos la precisión (accuracy) como puntaje.
    """
    k = max(1, int(solution[0])) # K debe ser al menos 1
    
    # Modelo de Scikit-learn
    modelo = KNeighborsClassifier(n_neighbors=k)
    modelo.fit(X_train, y_train)
    
    # El fitness es la precisión del modelo con esos parámetros
    return modelo.score(X_test, y_test)

# 3. Configuración del Algoritmo Genético
ga_instance = pygad.GA(
    num_generations=20,          # Número de generaciones (evolución)
    num_parents_mating=4,        # Padres para el cruce
    fitness_func=fitness_func,   # Nuestra función de evaluación
    sol_per_pop=8,               # Individuos por población
    num_genes=1,                 # Genes: solo buscamos 1 valor (K)
    gene_space=[range(1, 30)],   # El espacio de búsqueda (K entre 1 y 30)
    parent_selection_type="sss", # Tipo de selección
    crossover_type="single_point",
    mutation_type="random",
    mutation_percent_genes=10
)

# 4. Ejecución
print("Iniciando optimización genética...")
ga_instance.run()

# 5. Resultados
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print(f"Mejor valor de K encontrado: {int(solution[0])}")
print(f"Precisión del modelo con ese K: {solution_fitness}")