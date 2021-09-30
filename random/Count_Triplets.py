def countTriplets(arr, r):
    total = 0
    print(arr, r)
    arr_dict = {}

    for i in arr:
        if i in arr_dict:
            arr_dict[i] += 1
        else:
            arr_dict[i] = 1

    for i in range(len(arr)):
        first_element = arr[i]
        second_element = first_element * r
        third_element = second_element * r

        if second_element and third_element in arr_dict:
            total += arr_dict[second_element] * arr_dict[third_element]
    return total


nr = input().rstrip().split()
n = int(nr[0])
r = int(nr[1])
arr = list(map(int, input().rstrip().split()))
print(countTriplets(arr,r))