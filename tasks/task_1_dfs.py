"""
Задание 1: Поиск в глубину (DFS)
Примените алгоритм поиска в глубину к приведённому графу.
Записать время начала и время конца обработки каждой вершины (pre- и post-значения).
Пометьте каждое ребро как древесное, прямое, обратное или перекрёстное.
"""

from typing import Dict, List, Tuple, Set


class DFSGraph:
    def __init__(self):
        self.vertices: Set[str] = set()
        self.edges: List[Tuple[str, str]] = []
        self.adjacency_list: Dict[str, List[str]] = {}

    def add_edge(self, u: str, v: str):
        """Добавить ребро в граф"""
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []

        self.adjacency_list[u].append(v)
        self.vertices.add(u)
        self.vertices.add(v)
        self.edges.append((u, v))

    def dfs(self) -> Tuple[Dict, Dict, Dict]:
        """
        Выполнить поиск в глубину
        Возвращает: pre-значения, post-значения, классификация ребер
        """
        visited = set()
        pre_time = {}
        post_time = {}
        edge_types = {}
        time_counter = [0]  # Используем список для изменения в вложенной функции

        def dfs_visit(vertex: str, parent: str = None):
            visited.add(vertex)
            time_counter[0] += 1
            pre_time[vertex] = time_counter[0]

            for neighbor in self.adjacency_list.get(vertex, []):
                edge_key = (vertex, neighbor)

                if neighbor not in visited:
                    # Древесное ребро
                    edge_types[edge_key] = "Древесное"
                    dfs_visit(neighbor, vertex)
                else:
                    # Классифицируем остальные ребра
                    if pre_time.get(neighbor, float('inf')) > pre_time[vertex]:
                        edge_types[edge_key] = "Прямое"
                    elif neighbor not in post_time:
                        edge_types[edge_key] = "Обратное"
                    else:
                        edge_types[edge_key] = "Перекрёстное"

            time_counter[0] += 1
            post_time[vertex] = time_counter[0]

        # Запустить DFS для всех вершин
        for vertex in sorted(self.vertices):
            if vertex not in visited:
                dfs_visit(vertex)

        return pre_time, post_time, edge_types


def run_task_1():
    """Запустить Задание 1"""
    print("\n" + "="*60)
    print("ЗАДАНИЕ 1: Поиск в глубину (DFS)")
    print("="*60)

    graph = DFSGraph()

    print("\nВвведите граф. Формат: u v (где u и v - вершины)")
    print("Введите пустую строку для завершения ввода графа\n")

    while True:
        try:
            edge_input = input("Ребро (u v): ").strip()
            if not edge_input:
                break

            parts = edge_input.split()
            if len(parts) != 2:
                print("Ошибка: введите ровно две вершины (u v)")
                continue

            u, v = parts[0], parts[1]
            graph.add_edge(u, v)

        except EOFError:
            break
        except Exception as e:
            print(f"Ошибка ввода: {e}")

    if not graph.vertices:
        print("Граф пуст! Невозможно выполнить поиск.")
        return

    # Выполнить DFS
    pre_time, post_time, edge_types = graph.dfs()

    # Вывести результаты
    print("\n" + "-"*60)
    print("РЕЗУЛЬТАТЫ:")
    print("-"*60)

    print("\nВремя обработки вершин (pre- и post-значения):")
    print(f"{'Вершина':<10} {'Pre-значение':<15} {'Post-значение':<15}")
    print("-" * 40)

    for vertex in sorted(pre_time.keys()):
        print(f"{vertex:<10} {pre_time[vertex]:<15} {post_time[vertex]:<15}")

    print("\nКлассификация ребер:")
    print(f"{'Ребро':<15} {'Тип':<20}")
    print("-" * 35)

    for edge in graph.edges:
        edge_key = tuple(edge)
        if edge_key in edge_types:
            edge_str = f"{edge[0]} → {edge[1]}"
            print(f"{edge_str:<15} {edge_types[edge_key]:<20}")

    print("\n" + "="*60)


if __name__ == "__main__":
    run_task_1()

