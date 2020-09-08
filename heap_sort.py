
"""

堆排序的步骤：
1.建堆，从上往下

"""


def sift(li, low, high):
    """
    ：param  li: 列表
    : param  low : 堆的根节点位置（父节点）
    ：param  hgih: 堆的最后一个元素的位置
    ：return 
    """ 
i  = low   # i最开始指向根节点
j  = 2 * i + 1  # j开始是左孩子，j+1是右节点
tmp = li[low] # 把堆顶存起来
while j <= high : #只要j位置有数
    if j + 1 <= high and  li[j+1] > li[j] :  #1.存在右节点且，右节点比左节点大
        j = j + 1 # j指向右节点
    if li[j] > tmp :
        li[i] = li[j]
        i = j
        j = 2 * i + 1
    else:   # tmp 更大，把tmp放到i的位置上
        li[i] = tmp    #把tmp放到某一节点上
        break

else:
    li[i] = tmp #把拿出来进行对比的数字放回去。

def heap_sort(li):
    n = len(li)
    for i in range((n - 2)//2, -1, -1)
    # i表示建堆的时候调整的根的下标
        sift(li,i,n-1)

    #堆建完了
    print(li)




li = [ i for i in range(100)]
import random
random.shuffle(li)
heap_sort(li)
