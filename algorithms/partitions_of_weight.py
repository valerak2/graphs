from algorithms.check_correct_graph import is_graphical_partition


def get_all_graphical_partitions(weight: int):
    """
    Функция возвращает список всех графических разбиений заданного веса
    """
    max_vertex_weight = weight // 2
    return generate_all_partitions(weight, max_vertex_weight)


def generate_all_partitions(weight, max_vertex_weight, partition=[], graphical_partitions=[]):
    """
    Рекурсивный алгоритм получения всех возможных разбиенией заданного веса
    Жутко медленный
    """
    if weight < 0:
        return 0
    if weight == 0:
        check_is_graph(partition, graphical_partitions)
        return 1
    for i in range(1, min(weight + 1, max_vertex_weight + 1)):
        new_partition = partition.copy()
        new_partition.append(i)
        generate_all_partitions(weight - i, max_vertex_weight, partition=new_partition)
    return graphical_partitions


def check_is_graph(partition: list, graphical_partition=[]):
    partition.sort(reverse=True)
    if partition not in graphical_partition:
        if is_graphical_partition(partition):
            graphical_partition.append(partition)
