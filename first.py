import random


def c_search(array: list, target, force: bool = False) -> int:
    """
    Binary search via (c)ycles
    Will always return an index if `force` is set to True
    Time  : O(log(n))
    Space : O(1)
    """
    west, east = 0, len(array) - 1
    while west <= east:
        center = (west + east) >> 1
        if array[center] < target:
            west = center + 1
        elif array[center] > target:
            east = center - 1
        else:
            return center
    return west if force else -1


def r_search(array: list, target) -> int:
    """
    Binary search via (r)ecursion
    Time  : O(log(n))
    Space : O(log(n)) (due to the extra calls)
    """
    if not array:
        return -1
    center = (len(array) - 1) >> 1
    if array[center] < target:
        r = r_search(array[center + 1 :], target)
        return r if r == -1 else (center + 1) + r
    elif array[center] > target:
        return r_search(array[:center], target)
    else:
        return center


def insertion_sort(array: list) -> list:
    """
    Insertion sorting algorithm utilizing binary search
    """
    for i in range(1, len(array)):
        j = c_search(array[:i], key := array[i], force=True)
        array.pop(i)
        array.insert(j, key)
    return array


def main():
    array = sorted(random.randint(0, 99) for _ in range(10))
    r = random.choice(array)

    _array = list(array)
    random.shuffle(_array)

    print("Изначальный массив    :", array)
    print("Перемешанный массив   :", _array)
    print()
    print(f"Индекс числа      {r: 3d} : {r_search(array, r): 2d}")
    print(f"Индекс числа      100 : {r_search(array, 100): 2d}")
    print()
    print("Встроенная сортировка :", sorted(_array))
    print("Наша сортировка       :", insertion_sort(_array))


if __name__ == "__main__":
    main()
