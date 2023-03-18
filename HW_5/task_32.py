def find_indexes(arr, min_value, max_value):
    indexes = []
    for i in range(len(arr)):
        if min_value <= arr[i] <= max_value:
            indexes.append(i)
    return indexes

my_array = [2, 5, 7, 10, 1, 9, 6, 3]
min_value = 3
max_value = 7
result = find_indexes(my_array, min_value, max_value)
print(f"Индексы элементов, значения которых в диапазоне от {min_value} до {max_value}: {result}")