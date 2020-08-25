def select_sort_simple(li):
    li_new = []
    for i in range(len(li)): #时间复杂度 O(N)
        min_val = min(li)       #时间复杂度 O(N)
        li_new.append(min_val)  
        li.remove(min_val)
    return li_new
 #时间复杂度 O(N^2)

def select_sort(li):
    for i in range(len(li)-1): # i是第几趟
        min_loc = i
        for j in range(i,len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc] , li[i]
        
        print(li)

        

li = [3, 4, 5, 1, 6, 7, 9, 8]
#print(select_sort_simple(li))
#print(li)
select_sort(li)
