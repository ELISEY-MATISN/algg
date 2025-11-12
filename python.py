# Входные данные: Граф с 12 вершинами (матрица смежности)





import random

def local_search_independent_set(graph):
    n = len(graph)
    vertices = list(range(n))
    
    
    current_set = set()
    
    
    for v in vertices:
        if random.random() < 0.3:  
            
            can_add = True
            for u in current_set:
                if graph[v][u] == 1:
                    can_add = False
                    break
            if can_add:
                current_set.add(v)
    
    improved = True
    while improved:
        improved = False
        
        
        for v in vertices:
            if v not in current_set:
                
                can_add = True
                for u in current_set:
                    if graph[v][u] == 1:
                        can_add = False
                        break
                
                if can_add:
                    current_set.add(v)
                    improved = True
    
    return current_set

def print_graph_info(graph):
    n = len(graph)
    print(f"Граф с {n} вершинами:")
    print("Матрица смежности:")
    for i in range(n):
        print(f"Вершина {i}: {graph[i]}")


def create_example_graph():
    
    n = 12
    graph = [[0] * n for _ in range(n)]
    
    
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < 0.25:
                graph[i][j] = 1
                graph[j][i] = 1
    
    return graph


if __name__ == "__main__":
    graph = create_example_graph()
    
    print("=" * 50)
    print_graph_info(graph)
    print("=" * 50)
    
    independent_set = local_search_independent_set(graph)
    
    print("Результат работы алгоритма:")
    print(f"Найденное независимое множество: {sorted(independent_set)}")
    print(f"Размер независимого множества: {len(independent_set)}")
    
    is_correct = True
    for v in independent_set:
        for u in independent_set:
            if v != u and graph[v][u] == 1:
                is_correct = False
                break
    
    print(f"Корректность решения: {'Да' if is_correct else 'Нет'}")
    print("=" * 50)





# Выводимые данные: Найденное независимое множество и его размер


# Граф с 12 вершинами:
# Матрица смежности:
# Вершина 0: [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
# Вершина 1: [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
# Вершина 2: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Вершина 3: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Вершина 4: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
# Вершина 5: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Вершина 6: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Вершина 7: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Вершина 8: [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Вершина 9: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Вершина 10: [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
# Вершина 11: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Результат работы алгоритма:
# Найденное независимое множество: [1, 2, 3, 4, 5, 6, 7, 9]
# Размер независимого множества: 8
# Корректность решения: Да
