"""
Задание 2: Поиск в ширину (BFS)
Примените алгоритм поиска в ширину к приведённому графу.
Определить цикличность и ацикличность графа.
Исключить все дуги не входящие в цикл.
"""

from typing import Dict, List, Tuple, Set
from collections import deque


class BFSGraph:
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

    def bfs(self, start: str) -> Tuple[Dict[str, int], Dict[str, str]]:
        """
        Выполнить поиск в ширину
        Возвращает: расстояния, родители вершин
        """
        distances = {v: float('inf') for v in self.vertices}
        parent = {v: None for v in self.vertices}
        distances[start] = 0

        queue = deque([start])

        while queue:
            u = queue.popleft()
            for v in self.adjacency_list.get(u, []):
                if distances[v] == float('inf'):
                    distances[v] = distances[u] + 1
                    parent[v] = u
                    queue.append(v)

        return distances, parent

    def has_cycle(self) -> bool:
        """Определить наличие цикла в графе"""
        visited = set()
        rec_stack = set()

        def has_cycle_dfs(vertex):
            visited.add(vertex)
            rec_stack.add(vertex)

            for neighbor in self.adjacency_list.get(vertex, []):
                if neighbor not in visited:
                    if has_cycle_dfs(neighbor):
                        return True
                elif neighbor in rec_stack:
                    return True

            rec_stack.remove(vertex)
            return False

        for vertex in self.vertices:
            if vertex not in visited:
                if has_cycle_dfs(vertex):
                    return True

        return False

    def get_cycle_edges(self) -> List[Tuple[str, str]]:
        """Получить только ребра, входящие в циклы"""
        visited = set()
        rec_stack = set()
        cycle_edges = set()

        def find_cycle_edges(vertex, path):
            visited.add(vertex)
            rec_stack.add(vertex)

            for neighbor in self.adjacency_list.get(vertex, []):
                if neighbor not in visited:
                    path.append(neighbor)
                    find_cycle_edges(neighbor, path)
                    path.pop()
                elif neighbor in rec_stack:
                    # Найден цикл
                    try:
                        idx = path.index(neighbor)
                        for i in range(idx, len(path)):
                            if i < len(path) - 1:
                                cycle_edges.add((path[i], path[i + 1]))
                            cycle_edges.add((path[-1], neighbor))
                    except ValueError:
                        pass

            rec_stack.remove(vertex)

        for vertex in self.vertices:
            if vertex not in visited:
                find_cycle_edges(vertex, [vertex])

        return list(cycle_edges)


def run_task_2():
    """Запустить Задание 2"""
    print("\n" + "="*60)
    print("ЗАДАНИЕ 2: Поиск в ширину (BFS)")
    print("="*60)

    graph = BFSGraph()

    print("\nВведите граф. Формат: u v (где u и v - вершины)")
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

    # Выполнить BFS
    start_vertex = sorted(graph.vertices)[0]
    distances, parent = graph.bfs(start_vertex)

    # Проверить цикличность
    is_cyclic = graph.has_cycle()

    # Вывести результаты
    print("\n" + "-"*60)
    print("РЕЗУЛЬТАТЫ:")
    print("-"*60)

    print(f"\nОбход в ширину начиная с вершины '{start_vertex}':")
    print(f"{'Вершина':<10} {'Расстояние':<15} {'Родитель':<15}")
    print("-" * 40)

    for vertex in sorted(distances.keys()):
        dist = distances[vertex] if distances[vertex] != float('inf') else "∞"
        par = parent[vertex] if parent[vertex] else "—"
        print(f"{vertex:<10} {str(dist):<15} {par:<15}")

    print(f"\nЦикличность графа: {'ЦИКЛИЧЕСКИЙ' if is_cyclic else 'АЦИКЛИЧЕСКИЙ'}")

    if is_cyclic:
        cycle_edges = graph.get_cycle_edges()
        print(f"\nРебра, входящие в циклы: {len(cycle_edges)} шт.")
        for edge in cycle_edges:
            print(f"  {edge[0]} → {edge[1]}")

        print(f"\nВсего ребер в графе: {len(graph.edges)}")
        print(f"Ребра НЕ входящие в циклы: {len(graph.edges) - len(cycle_edges)} шт.")
        non_cycle_edges = [e for e in graph.edges if tuple(e) not in [(ce[0], ce[1]) for ce in cycle_edges]]
        for edge in non_cycle_edges:
            print(f"  {edge[0]} → {edge[1]}")
    else:
        print("\nВсе ребра НЕ входят в циклы (граф ациклический)")

    print("\n" + "="*60)


if __name__ == "__main__":
    run_task_2()

