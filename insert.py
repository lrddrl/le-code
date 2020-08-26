def insert_sort(li):
    for i in range(1,len(li)): #i 表示摸到的牌的下标
        tmp = li[i]
        j = i - 1 #j 指的是手里的牌的下标
        while j>=0 and li[j] > tmp: 
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp
        print(li)
        
li = [4,1,5,2,9,7,7]
insert_sort(li)
