arr1 = ["A", "B", "C", "A", "B"]

print(arr1)


def first_recurring(arr):
    counts = {}
    for char in arr:
        if char in counts:
            return char
        counts[char] = 1
    return None


print(first_recurring(arr1))