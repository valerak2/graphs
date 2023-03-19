from auxiliary_operations import calculate_tl, calculate_r, calculate_hd, correct_partition
from algorithms.check_correct_graph import is_graphical_partition


class Graphical_partition:
    """Класс графического разбиения содержащий само разбиение и операция с этим разбиением"""

    def __init__(self, partition: list):
        self.partition = partition

        self.r = calculate_r(partition)
        "Ранг Дерфи"

        self.hd = calculate_hd(partition, self.r)
        "Голова разбиения"

        self.tl = calculate_tl(partition, self.r)
        "Хвост разбиения"

        self.lenght_partition = len(partition)

    def get_height(self):
        """Высота - количество вращений до ближайшего порогового графа"""
        diff = self.component_difference()
        h = 0
        for i in diff:
            h += abs(i)
        return h // 2

    def is_tl_equal_hd(self):
        correct_partition(self.tl, self.hd)
        return self.tl == self.hd

    def component_difference(self):
        """Покомпонентная разность двух разбиений"""
        correct_partition(self.tl, self.hd)
        diff = [x - y for x, y in zip(self.tl, self.hd)]
        return diff

    def down_edge_rotation(self, index_from, index_in):
        """Понижающее вращение, соответствующее перекидыванию блока вниз по диаграмме Ферре"""
        arr = self.partition.copy()
        if index_in == len(arr):
            arr.append(0)
        if (index_from < index_in and
                (arr[index_from] >= arr[index_in] + 2) and
                (index_from + 1 <= len(arr) and
                 arr[index_from] > 1 and
                 (arr[index_from] > arr[index_from + 1]) and
                 arr[index_from] <= arr[index_from - 1]) and
                arr[index_in] < arr[index_in - 1]):

            arr[index_from] -= 1
            arr[index_in] += 1
            return Graphical_partition(arr)
        else:
            print(f"туда нельзя вращать "
                  f"from:{index_from} in:{index_in} "
                  )

    def up_edge_rotation(self, index_from, index_in):
        """Повышающее вращение, соответствующее перекидыванию блока вверх по диаграмме Ферре"""
        arr = self.partition.copy()
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
            if is_graphical_partition(arr):
                return Graphical_partition(arr)
            else:
                print("Получилось не графическое разбиение")
        else:
            print(f"туда нельзя вращать "
                  f"from:{index_from} in:{index_in} "
                  )

    def preserving_edge_rotation(self, index_from, index_in):
        """Сохраняющее вращение"""
        pass

    def get_all_up_partitions(self):
        up_partitions = []
        for i in range(self.lenght_partition):
            if self.partition[i] != 0:
                for j in range(self.lenght_partition - i):
                    p = self.partition.copy()
                    p[j] += 1
                    p[-i - 1] -= 1
                    p = [i for i in p if i != 0]
                    new_p = sorted(p, reverse=True)
                    if is_graphical_partition(new_p) \
                            and \
                            new_p not in up_partitions and new_p != self.partition:
                        up_partitions.append(new_p)

    def get_all_preserving_partitions(self):
        pass

    def draw_graph(self):
        pass
