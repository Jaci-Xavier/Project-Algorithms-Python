def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return (sort_string(first_string), sort_string(second_string), False)

    sorted_first = sort_string(first_string)
    sorted_second = sort_string(second_string)

    return (sorted_first, sorted_second, sorted_first == sorted_second)


def merge_sort(strings):
    if len(strings) <= 1:
        return strings

    mid = len(strings) // 2
    left = strings[:mid]
    right = strings[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result


def sort_string(input_string):
    input_string = input_string.lower()
    input_string = list(input_string)
    sorted_string = "".join(merge_sort(input_string))
    return sorted_string
