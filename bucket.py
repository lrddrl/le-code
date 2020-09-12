def bucket_sort(li, n=100, max_num=10000)
    buckets = [[for _ in range(n)] #创建桶
    for var in li:
        i = min( var // (max_num // n), n-1) #i标志var放到几号桶里
        bucket[i].append(var)
        for j in range(len(buckets[i]-1, 0, -1))
        if 