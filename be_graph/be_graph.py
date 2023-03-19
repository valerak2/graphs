import sys
from pyvis.network import Network


# Примеры входных данных:
# 3 2 2 2 2 2 1 1 1
# 3 2 2 2 1
# 3 3 2 2 2
# 5 5 5 3 3 3 3 3

def main():
    with open("input", "r") as file:
        input_str = file.readline()
        if input_str == "":
            print("Файл входных аргументов input.txt пуст")
            return
        list_of_valence = list(map(int, (input_str.split(" "))))
    check_existence(list_of_valence)
    check_that_connected(list_of_valence)
    print(get_subseq(list_of_valence))
    subseqs_0 = get_subseq(list_of_valence)

    counter = 0
    for subseq in subseqs_0:
        res = build_graph(list_of_valence, subseq, counter)
        counter += 1
        print(res)


def check_that_connected(input_list):
    if sum(input_list) < 2 * (len(input_list) - 1):
        print("Нельзя построить связный граф.")
        sys.exit()
    else:
        print("Можно построить связный граф")


def check_existence(input_list):
    if sum(input_list) % 2 != 0:
        print("Сумма всех членов графической последовательности нечетна!")
        sys.exit()
    if input_list[0] > len(input_list) - 1:
        print("Простой граф построить нельзя!")
        sys.exit()
    check_Erdos_Gallai_criterion(input_list)


def check_Erdos_Gallai_criterion(input_list):
    for k in range(len(input_list) - 1):
        if sum(input_list[:k + 1]) > (k * (k + 1)) + get_sum_of_min(k, input_list):
            print("Критерий Эрдёша—Галлаи не выполнен!")
            print("Последовательность не является графической")
            sys.exit()
    print("Критерий Эрдёша—Галлаи выполняется")
    print("Следовательно, последовательность является графической")


def get_sum_of_min(k, c_list):
    acc = 0
    for i in range(k + 1, len(c_list)):
        acc += min(k + 1, c_list[i])
    return acc


def get_subseq(input_list):
    result = []
    length = len(input_list)
    half = sum(input_list) // 2
    sub_0 = [input_list[0]]
    skip = []
    i = 1
    while i < length:
        item = input_list[i]
        if input_list[0] + item > half:
            i += 1
            continue
        if input_list[0] + item == half:
            list_to_append = sub_0.copy()
            list_to_append.append(item)
            result.append(list_to_append)
            i += 1
            continue
        sub_0.append(item)
        j = i + 1
        while j < length:
            nested_item = input_list[j]
            sum_sub_0 = sum(sub_0)
            if nested_item in skip:
                j += 1
                continue
            if sum_sub_0 + nested_item > half:
                skip.append(nested_item)
                j += 1
                continue
            if sum_sub_0 + nested_item == half:
                sub_0.append(nested_item)
                result.append(sub_0)
                sub_0 = sub_0[:2]
                skip.append(nested_item)
                j = i + 1
                continue
            sub_0.append(nested_item)
            j += 1
        sub_0 = [input_list[0]]
        skip.clear()
        i += 1

    final = []
    for item in result:
        if not (item in final):
            final.append(item)
    return final


def build_graph(list_of_valence, subseq_0, k):
    length = len(list_of_valence)
    subseq_1 = get_couple_subseq(list_of_valence, subseq_0)
    is_ok = check_subseq_corr(subseq_0, subseq_1)
    if not is_ok:
        return None

    net = Network()
    number = 0
    for item in subseq_0:
        net.add_node(number, label=f"{number}")
        number += 1
    start_seq1 = number

    for _ in subseq_1:
        net.add_node(number,  label=f"{number}")
        number += 1

    free_valence_subseq_1 = subseq_1.copy()
    for item in range(len(subseq_0) - 1, -1, -1):
        n = len(subseq_1) - 1
        valence = subseq_0[item]
        while valence > 0:
            index_of_max_el = free_valence_subseq_1.index((max(free_valence_subseq_1)))
            free_valence_subseq_1[index_of_max_el] -= 1
            valence -= 1
            net.add_edge(item, index_of_max_el + start_seq1)

    net.show("basic{}.html".format(k))


def check_subseq_corr(seq_0, seq_1):
    seq_0_len = len(seq_0)
    seq_1_len = len(seq_1)

    seq_0_max = seq_0[0]
    seq_1_max = seq_1[0]

    if seq_0_len < seq_1_max or seq_1_len < seq_0_max:
        return False
    return True


def get_couple_subseq(input_list, subseq):
    result = input_list.copy()
    for item in subseq:
        result.remove(item)
    return result


def build_graph_by_Hakimi(i_list):
    work_list = i_list.copy()
    fixed_vertex = work_list.pop(0)
    for index in range(fixed_vertex):
        work_list[index] = work_list[index] - 1
    work_list.sort(reverse=True)
    if work_list[0] == 0:
        print("Граф построен")
        sys.exit()
    while True:
        if work_list[-1] == 0:
            del work_list[-1]
        else:
            break
    build_graph_by_Hakimi(work_list)


if __name__ == '__main__':
    main()
