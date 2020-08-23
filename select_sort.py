def select_sort_simple(li):
    li_new = []
    for i in range(len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new


def select_sort(li):
    for i in range(len(li)-1):
        

li = [3, 4, 5, 1, 6, 7, 9, 8]
print(select_sort_simple(li))
