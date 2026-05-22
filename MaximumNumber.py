# find the Maximum Number in a list

def find_max(arr):
    max_num = arr[0]

    for i in arr:
        if i > max_num:
            max_num = i

    return max_num


arr = list(map(int, input("Enter numbers separated by space: ").split()))
print(find_max(arr))