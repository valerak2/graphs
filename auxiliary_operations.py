def calculate_r(partition: list):
    for i in range(len(partition)):
        if (partition[i] >= i) \
                and \
                (partition[i + 1] <= (i + 1)):
            return i + 1


def calculate_hd(partition: list, r: int):
    hd = []
    for i in range(r):
        el = partition[i] - r + 1
        hd.append(el)
    return hd


def calculate_tl(partition: list, r: int):
    partition = partition[r:]
    tl = []
    for i in range(partition[0]):
        tl.append(len(partition))
        partition = [x - 1 for x in partition if x - 1 > 0]
    return tl


def correct_partition(first_p: list, second_p: list):
    """Функция выравнивает количество элементов списков разбиений, заполняя их 0"""
    l_first_p = len(first_p)
    l_second_p = len(second_p)
    if l_first_p > l_second_p:
        diff = l_first_p - l_second_p
        for i in range(diff):
            second_p.append(0)
    elif l_first_p < l_second_p:
        diff = l_second_p - l_first_p
        for i in range(diff):
            first_p.append(0)
    else:
        return
