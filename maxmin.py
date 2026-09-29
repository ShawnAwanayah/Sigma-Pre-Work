def maxmin(lst: list):
    new_list = []
    if len(lst) == 1:
        return lst
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    new_list.append(lst[0])
    new_list.append(lst[-1])
    return new_list
