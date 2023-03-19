def Erdos_Gallai_criterion(input_list):
    for k in range(len(input_list) - 1):
        if sum(input_list[:k + 1]) > (k * (k + 1)) + get_sum_of_min(k, input_list):
            return False
        else:
            continue
    return True


def get_sum_of_min(k, c_list):
    acc = 0
    for i in range(k + 1, len(c_list)):
        acc += min(k + 1, c_list[i])
    return acc


def algorithm_Havel_Hakimi(partition):
    if partition[0] < len(partition):
        i = partition[0]
        if i == 0:
            return True
        else:
            new_partition = []
            for j in range(1, len(partition)):
                if i > 0:
                    number = partition[j] - 1
                    if number < 0:
                        return False
                    i -= 1
                else:
                    number = partition[j]
                new_partition.append(number)
            new_partition.sort(reverse=True)
            if is_graphical_partition(new_partition):
                return True
            else:
                return False


def is_graphical_partition(partition):
    if (sum(partition) % 2) == 0:
        return algorithm_Havel_Hakimi(partition)
        # return Erdos_Gallai_criterion()
    else:
        return False
