from graphical_partition import Graphical_partition

max_partitions = []


class search_max_graphical_partitions:
    """Алгоритм поиска всех ближайших максимальных графических разбиений для заданного разбиения"""
    def __init__(self, gp: Graphical_partition):
        self.gp = gp
        self.diff = gp.component_difference()
        self.max_partitions = []

    def alghorithm(self):
        dfs(self.gp)
        self.max_partitions = max_partitions

    def get_max_partitions(self):
        self.alghorithm()
        return max_partitions


def dfs(gp: Graphical_partition):
    diff = gp.component_difference()

    up_tl_to_tl(diff, gp)
    up_tl_to_hd(diff, gp)
    up_hd_to_hd(diff, gp)

    down_hd_to_hd(diff, gp)
    down_hd_to_tl(diff, gp)
    down_tl_to_tl(diff, gp)

    if gp.is_tl_equal_hd() and (gp.partition not in max_partitions):
        max_partitions.append(gp.partition)


def up_tl_to_tl(diff, gp: Graphical_partition):
    negative = []
    for index, value in enumerate(diff):
        if value < 0:
            negative.append(index)
    if negative:
        for n in negative:
            for i in range(n):
                if diff[i] > 0:
                    real_index_n = gp.lenght_partition - (gp.tl[0] - gp.tl[n])
                    real_index_i = gp.lenght_partition - (gp.tl[0] - gp.tl[i]) - 1
                    new_gp = up_edge_rotation(gp, real_index_i, real_index_n)
                    if new_gp is not None:
                        dfs(new_gp)


def up_tl_to_hd(diff, gp: Graphical_partition):
    positive = []
    for index, value in enumerate(diff):
        if value > 0:
            positive.append(index)
    if positive:
        for n in positive:
            for i in range(len(gp.tl)):
                if diff[i] > 0:
                    if n == i and diff[i] % 2 != 0:
                        continue
                    real_index_n = n
                    real_index_i = gp.lenght_partition - (gp.tl[0] - gp.tl[i]) - 1
                    new_gp = up_edge_rotation(gp, real_index_i, real_index_n)
                    if new_gp is not None:
                        dfs(new_gp)


def up_hd_to_hd(diff, gp: Graphical_partition):
    excess = []
    for index, value in enumerate(diff):
        if value < 0:
            excess.append(index)
    if excess:
        for n in excess:
            for i in range(n):
                if diff[i] > 0:
                    new_gp = up_edge_rotation(gp, n, i)
                    if new_gp is not None:
                        dfs(new_gp)


def down_hd_to_hd(diff, gp: Graphical_partition):
    excess = []
    for index, value in enumerate(diff):
        if value < 0 and index < len(gp.hd) - 1:
            excess.append(index)
    if excess:
        for n in excess:
            for i in range(n + 1, len(gp.hd)):
                if diff[i] > 0:
                    new_gp = down_edge_rotation(gp, n, i)
                    if new_gp is not None:
                        dfs(new_gp)


def down_hd_to_tl(diff, gp: Graphical_partition):
    excess = []
    for index, value in enumerate(diff):
        if value < 0:
            excess.append(index)
    if excess:
        for n in excess:
            for i in range(len(gp.tl)):
                if n == i and diff[i] % 2 != 0:
                    continue
                if diff[i] < 0:
                    real_index_i = gp.lenght_partition - (gp.tl[0] - gp.tl[i])
                    new_gp = down_edge_rotation(gp, n, real_index_i)
                    if new_gp is not None:
                        dfs(new_gp)


def down_tl_to_tl(diff, gp: Graphical_partition):
    excess = []
    for index, value in enumerate(diff):
        if value < 0 and index < len(gp.tl) - 1:
            excess.append(index)
    if excess:
        for n in excess:
            for i in range(n + 1, len(gp.tl)):
                if diff[i] > 0:
                    real_index_n = gp.lenght_partition - (gp.tl[0] - gp.tl[n])
                    real_index_i = gp.lenght_partition - (gp.tl[0] - gp.tl[i]) - 1
                    new_gp = down_edge_rotation(gp, real_index_i, real_index_n)
                    if new_gp is not None:
                        dfs(new_gp)


def down_edge_rotation(g: Graphical_partition, index_from, index_in):
    arr = g.partition.copy()
    if index_in == len(arr):
        arr.append(0)
    if (index_from < index_in and
            (arr[index_from] >= arr[index_in] + 2) and
            (index_from + 1 <= len(arr) and
             arr[index_from] > 1 and
             (arr[index_from] > arr[index_from + 1]) and
             arr[index_from] <= arr[index_from - 1]) and
            arr[index_in] < arr[index_in - 1]
    ):
        arr[index_from] -= 1
        arr[index_in] += 1
        return Graphical_partition(arr)


def up_edge_rotation(g: Graphical_partition, index_from, index_in):
    arr = g.partition.copy()
    if (arr[index_in] >= arr[index_from] and
            ((index_in == 0 and arr[index_in] >= arr[index_in + 1]) or
             (index_in != 0 and arr[index_in + 1] <= arr[index_in] < arr[index_in - 1])) and
            ((index_from == len(arr) - 1) or
             (index_from != len(arr) - 1 and arr[index_from] > arr[index_from + 1]

             ))):
        arr[index_from] -= 1
        if arr[index_from] == 0:
            arr.remove(arr[index_from])
        arr[index_in] += 1
        return Graphical_partition(arr)
