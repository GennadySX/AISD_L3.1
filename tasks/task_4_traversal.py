"""
Задание 4: Обход графа
Записать последовательность вершин при прямом, симметричном и обратном обходе графа
"""

from typing import Dict, List, Set
from collections import deque


class TreeGraph:
    def __init__(self):
        self.vertices: Set[str] = set()
        self.edges: List[tuple] = []
        self.adjacency_list: Dict[str, List[str]] = {}
        self.is_binary_tree = False

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

    def build_tree_from_edges(self) -> Dict[str, List[str]]:
        """Построить дерево из ребер (для обхода дерева)"""
        # Для простоты предполагаем, что граф - это дерево
        # Выберем корень как вершину с наименьшим именем
        tree = {v: [] for v in self.vertices}

        # Найти корень (вершина без входящих ребер)
        in_degree = {v: 0 for v in self.vertices}
        for u, v in self.edges:
            in_degree[v] += 1

        root = None
        for vertex in sorted(self.vertices):
            if in_degree[vertex] == 0:
                root = vertex
                break

        if root is None:
            root = sorted(self.vertices)[0]

        # Построить дерево
        visited = set()

        def build_tree(node):
            visited.add(node)
            for neighbor in self.adjacency_list.get(node, []):
                if neighbor not in visited:
                    tree[node].append(neighbor)
                    build_tree(neighbor)

        build_tree(root)
        return tree, root

    def inorder_traversal(self, node: str, tree: Dict[str, List[str]], result: List[str]):
        """Симметричный (внутренний) обход дерева"""
        if not tree[node]:
            result.append(node)
            return

        # Для дерева: левое поддерево - родитель - правое поддерево
        if len(tree[node]) > 0:
            self.inorder_traversal(tree[node][0], tree, result)
        result.append(node)
        if len(tree[node]) > 1:
            self.inorder_traversal(tree[node][1], tree, result)

    def preorder_traversal(self, node: str, tree: Dict[str, List[str]], result: List[str]):
        """Прямой (префиксный) обход дерева"""
        result.append(node)
        for child in tree[node]:
            self.preorder_traversal(child, tree, result)

    def postorder_traversal(self, node: str, tree: Dict[str, List[str]], result: List[str]):
        """Обратный (постфиксный) обход дерева"""
        for child in tree[node]:
            self.postorder_traversal(child, tree, result)
        result.append(node)

    def breadth_first_traversal(self, root: str, tree: Dict[str, List[str]]) -> List[str]:
        """Обход в ширину (BFS)"""
        result = []
        queue = deque([root])
        visited = set([root])

        while queue:
            node = queue.popleft()
            result.append(node)
            for child in tree[node]:
                if child not in visited:
                    visited.add(child)
                    queue.append(child)

        return result


def run_task_4():
    """Запустить Задание 4"""
    print("\n" + "="*60)
    print("ЗАДАНИЕ 4: Обход графа (дерева)")
    print("="*60)

    graph = TreeGraph()

    print("\nВведите граф как дерево.")
    print("Формат: parent child (где parent - родитель, child - потомок)")
    print("Введите пустую строку для завершения ввода графа\n")

    while True:
        try:
            edge_input = input("Ребро (parent child): ").strip()
            if not edge_input:
                break

            parts = edge_input.split()
            if len(parts) != 2:
                print("Ошибка: введите ровно две вершины (parent child)")
                continue

            u, v = parts[0], parts[1]
            graph.add_edge(u, v)

        except EOFError:
            break
        except Exception as e:
            print(f"Ошибка ввода: {e}")

    if not graph.vertices:
        print("Граф пуст! Невозможно выполнить обход.")
        return

    # Построить дерево
    tree, root = graph.build_tree_from_edges()

    # Выполнить обходы
    preorder_result = []
    graph.preorder_traversal(root, tree, preorder_result)

    inorder_result = []
    graph.inorder_traversal(root, tree, inorder_result)

    postorder_result = []
    graph.postorder_traversal(root, tree, postorder_result)

    breadth_first_result = graph.breadth_first_traversal(root, tree)

    # Вывести результаты
    print("\n" + "-"*60)
    print("РЕЗУЛЬТАТЫ:")
    print("-"*60)

    print(f"\nКорень дерева: {root}")
    print(f"Всего вершин: {len(graph.vertices)}")

    print(f"\n1. ПРЯМОЙ (ПРЕФИКСНЫЙ) ОБХОД:")
    print(f"   {' → '.join(preorder_result)}")

    print(f"\n2. СИММЕТРИЧНЫЙ (ВНУТРЕННИЙ) ОБХОД:")
    print(f"   {' → '.join(inorder_result)}")

    print(f"\n3. ОБРАТНЫЙ (ПОСТФИКСНЫЙ) ОБХОД:")
    print(f"   {' → '.join(postorder_result)}")

    print(f"\n4. ОБХОД В ШИРИНУ (BFS):")
    print(f"   {' → '.join(breadth_first_result)}")

    # Визуализация структуры дерева
    print(f"\n5. СТРУКТУРА ДЕРЕВА:")

    def print_tree(node: str, indent: int = 0):
        print("  " * indent + "├─ " + node)
        for child in tree[node]:
            print_tree(child, indent + 1)

    print_tree(root)

    print("\n" + "="*60)


if __name__ == "__main__":
    run_task_4()

