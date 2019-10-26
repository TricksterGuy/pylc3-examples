def remove_spaces(s):
    arr = list(s)
    p1 = 0
    p2 = 0
    while p2 < len(arr):
        if arr[p2] == ' ':
            p2 += 1
        arr[p1] = arr[p2]
        p1 += 1
        p2 += 1
    return ''.join(arr)

print remove_spaces("a man a plan a canal panama")
