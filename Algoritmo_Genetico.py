import numpy
import pygad
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import datasets


iris = datasets.load_iris()
X, y = iris.data, iris.target


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

def fitness_func(ga_instance, solution, solution_idx):

    k = max(1, int(solution[0])) # K debe ser al menos 1
    
    modelo = KNeighborsClassifier(n_neighbors=k)
    modelo.fit(X_train, y_train)
    
    return modelo.score(X_test, y_test)


ga_instance = pygad.GA(
    num_generations=20,          
    num_parents_mating=4,        
    fitness_func=fitness_func,   
    sol_per_pop=8,               
    num_genes=1,                 
    gene_space=[range(1, 30)],   
    parent_selection_type="sss", 
    crossover_type="single_point",
    mutation_type="random",
    mutation_percent_genes=10
)

print("Iniciando optimización genética...")
ga_instance.run()


solution, solution_fitness, solution_idx = ga_instance.best_solution()
print(f"Mejor valor de K encontrado: {int(solution[0])}")
print(f"Precisión del modelo con ese K: {solution_fitness}")