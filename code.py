a = list(map(int, input().split()))
# print(a)
if not a:
    print(0)
else:
    sum_dict = {}
    for i in range(len(a)):
        for j in range(i+1, len(a)+1):
            # print(a[i:j])
            sum_dict[tuple(a[i:j])] = sum(a[i:j])
    keys = list(sum_dict.keys())
    # print(keys)
    values = list(sum_dict.values())
    # print(values)
    max_sum_index = values.index(max(values))
    # print(max_sum_index)
    print(*keys[max_sum_index])
