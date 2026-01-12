"""
Задание 3: Алгоритм Дейкстры
Найти кратчайшие пути из вершины f в остальные вершины
на основе алгоритма Дейкстры.
"""

from typing import Dict, List, Tuple, Set
import heapq


class DijkstraGraph:
    def __init__(self):
        self.vertices: Set[str] = set()
        self.edges: Dict[Tuple[str, str], int] = {}
        self.adjacency_list: Dict[str, List[Tuple[str, int]]] = {}

    def add_edge(self, u: str, v: str, weight: int):
        """Добавить взвешенное ребро в граф"""
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []

        self.adjacency_list[u].append((v, weight))
        self.vertices.add(u)
        self.vertices.add(v)
        self.edges[(u, v)] = weight

    def dijkstra(self, start: str) -> Tuple[Dict[str, int], Dict[str, str]]:
        """
        Найти кратчайшие пути из start до всех остальных вершин
        Возвращает: расстояния, пути (как предпоследняя вершина)
        """
        distances = {v: float('inf') for v in self.vertices}
        distances[start] = 0
        previous = {v: None for v in self.vertices}

        pq = [(0, start)]  # (расстояние, вершина)
        visited = set()

        while pq:
            current_dist, current = heapq.heappop(pq)

            if current in visited:
                continue

            visited.add(current)

            if current_dist > distances[current]:
                continue

            for neighbor, weight in self.adjacency_list.get(current, []):
                if neighbor not in visited:
                    new_dist = current_dist + weight

                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        previous[neighbor] = current
                        heapq.heappush(pq, (new_dist, neighbor))

        return distances, previous

    def get_path(self, previous: Dict[str, str], start: str, end: str) -> List[str]:
        """Получить путь от start до end"""
        if previous[end] is None and end != start:
            return []

        path = []
        current = end
        while current is not None:
            path.append(current)
            current = previous[current]

        return path[::-1]


def run_task_3():
    """Запустить Задание 3"""
    print("\n" + "="*60)
    print("ЗАДАНИЕ 3: Алгоритм Дейкстры")
    print("="*60)

    graph = DijkstraGraph()

    print("\nВведите взвешенный граф.")
    print("Формат: u v weight (где u и v - вершины, weight - вес ребра)")
    print("Введите пустую строку для завершения ввода графа\n")

    while True:
        try:
            edge_input = input("Ребро (u v weight): ").strip()
            if not edge_input:
                break

            parts = edge_input.split()
            if len(parts) != 3:
                print("Ошибка: введите ровно две вершины и вес (u v weight)")
                continue

            u, v, weight_str = parts[0], parts[1], parts[2]
            try:
                weight = int(weight_str)
                if weight < 0:
                    print("Ошибка: вес должен быть неотрицательным")
                    continue
            except ValueError:
                print("Ошибка: вес должен быть числом")
                continue

            graph.add_edge(u, v, weight)

        except EOFError:
            break
        except Exception as e:
            print(f"Ошибка ввода: {e}")

    if not graph.vertices:
        print("Граф пуст! Невозможно выполнить поиск.")
        return

    # Выбрать начальную вершину
    print(f"\nДоступные вершины: {', '.join(sorted(graph.vertices))}")
    try:
        start_vertex = input("Введите начальную вершину (по умолчанию 'f'): ").strip()
    except EOFError:
        start_vertex = ""

    if not start_vertex:
        start_vertex = 'f'

    if start_vertex not in graph.vertices:
        print(f"Ошибка: вершина '{start_vertex}' не существует в графе")
        return

    # Выполнить Дейкстру
    distances, previous = graph.dijkstra(start_vertex)

    # Вывести результаты
    print("\n" + "-"*60)
    print(f"РЕЗУЛЬТАТЫ (кратчайшие пути из '{start_vertex}'):")
    print("-"*60)

    print(f"\n{'Вершина':<10} {'Расстояние':<15} {'Путь':<30}")
    print("-" * 55)

    for vertex in sorted(distances.keys()):
        dist = distances[vertex] if distances[vertex] != float('inf') else "∞"
        path = graph.get_path(previous, start_vertex, vertex)
        path_str = " → ".join(path) if path else "Недостижима"
        print(f"{vertex:<10} {str(dist):<15} {path_str:<30}")

    print("\n" + "="*60)


if __name__ == "__main__":
    run_task_3()

