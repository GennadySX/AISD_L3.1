#!/usr/bin/env python3
"""
Демонстрационный скрипт для тестирования всех 4 заданий
"""

import sys
sys.path.insert(0, 'tasks')

from task_1_dfs import DFSGraph as Graph1
from task_2_bfs import BFSGraph as Graph2
from task_3_dijkstra import DijkstraGraph as Graph3
from task_4_traversal import TreeGraph as Graph4


def demo_task_1():
    """Демонстрация Задания 1 - DFS"""
    print("\n" + "="*70)
    print("ДЕМОНСТРАЦИЯ ЗАДАНИЯ 1: Поиск в глубину (DFS)")
    print("="*70)

    graph = Graph1()
    edges = [('a', 'b'), ('a', 'c'), ('b', 'd'), ('c', 'd')]

    print("\nГраф:")
    for u, v in edges:
        graph.add_edge(u, v)
        print(f"  {u} → {v}")

    pre_time, post_time, edge_types = graph.dfs()

    print("\nРезультаты DFS:")
    print(f"{'Вершина':<10} {'Pre':<10} {'Post':<10}")
    print("-" * 30)
    for v in sorted(pre_time.keys()):
        print(f"{v:<10} {pre_time[v]:<10} {post_time[v]:<10}")

    print("\nКлассификация ребер:")
    for edge in edges:
        edge_key = tuple(edge)
        if edge_key in edge_types:
            print(f"  {edge[0]} → {edge[1]}: {edge_types[edge_key]}")


def demo_task_2():
    """Демонстрация Задания 2 - BFS"""
    print("\n" + "="*70)
    print("ДЕМОНСТРАЦИЯ ЗАДАНИЯ 2: Поиск в ширину (BFS)")
    print("="*70)

    graph = Graph2()
    edges = [('a', 'b'), ('a', 'c'), ('b', 'c'), ('b', 'd'), ('c', 'd')]

    print("\nГраф:")
    for u, v in edges:
        graph.add_edge(u, v)
        print(f"  {u} → {v}")

    start = sorted(graph.vertices)[0]
    distances, parent = graph.bfs(start)

    print(f"\nОбход в ширину начиная с '{start}':")
    print(f"{'Вершина':<10} {'Расстояние':<15} {'Родитель':<10}")
    print("-" * 35)
    for v in sorted(distances.keys()):
        dist = distances[v] if distances[v] != float('inf') else "∞"
        par = parent[v] if parent[v] else "—"
        print(f"{v:<10} {str(dist):<15} {par:<10}")

    is_cyclic = graph.has_cycle()
    print(f"\nГраф {'циклический' if is_cyclic else 'ациклический'}")


def demo_task_3():
    """Демонстрация Задания 3 - Дейкстра"""
    print("\n" + "="*70)
    print("ДЕМОНСТРАЦИЯ ЗАДАНИЯ 3: Алгоритм Дейкстры")
    print("="*70)

    graph = Graph3()
    edges = [('a', 'b', 4), ('a', 'c', 2), ('b', 'c', 1), ('b', 'd', 5), ('c', 'd', 8)]

    print("\nВзвешенный граф:")
    for u, v, w in edges:
        graph.add_edge(u, v, w)
        print(f"  {u} → {v} (вес: {w})")

    start = 'a'
    distances, previous = graph.dijkstra(start)

    print(f"\nКратчайшие пути из '{start}':")
    print(f"{'Вершина':<10} {'Расстояние':<15}")
    print("-" * 25)
    for v in sorted(distances.keys()):
        dist = distances[v] if distances[v] != float('inf') else "∞"
        print(f"{v:<10} {str(dist):<15}")


def demo_task_4():
    """Демонстрация Задания 4 - Обход дерева"""
    print("\n" + "="*70)
    print("ДЕМОНСТРАЦИЯ ЗАДАНИЯ 4: Обход графа (дерева)")
    print("="*70)

    graph = Graph4()
    edges = [('a', 'b'), ('a', 'c'), ('b', 'd'), ('b', 'e'), ('c', 'f')]

    print("\nДерево:")
    for u, v in edges:
        graph.add_edge(u, v)
        print(f"  {u} → {v}")

    tree, root = graph.build_tree_from_edges()

    # Обходы
    preorder = []
    graph.preorder_traversal(root, tree, preorder)

    inorder = []
    graph.inorder_traversal(root, tree, inorder)

    postorder = []
    graph.postorder_traversal(root, tree, postorder)

    bfs_result = graph.breadth_first_traversal(root, tree)

    print(f"\nКорень: {root}")
    print(f"Прямой обход (pre-order): {' → '.join(preorder)}")
    print(f"Симметричный обход (in-order): {' → '.join(inorder)}")
    print(f"Обратный обход (post-order): {' → '.join(postorder)}")
    print(f"Обход в ширину (BFS): {' → '.join(bfs_result)}")


if __name__ == "__main__":
    print("\n" + "="*70)
    print("ДЕМОНСТРАЦИЯ ВСЕХ ЗАДАНИЙ AISD_L3")
    print("="*70)

    try:
        demo_task_1()
        demo_task_2()
        demo_task_3()
        demo_task_4()

        print("\n" + "="*70)
        print("✓ ВСЕ ДЕМОНСТРАЦИИ ВЫПОЛНЕНЫ УСПЕШНО")
        print("="*70 + "\n")

    except Exception as e:
        print(f"\n✗ Ошибка: {e}")
        import traceback
        traceback.print_exc()

