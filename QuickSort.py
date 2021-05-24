def Partition(A,left,right):    # 피봇을 정해주고 피봇에 순서에 따라 나눠줌
    p = A[left]
    low = left
    high = right
    while low < high:
        low+=1
        while p > A[low] and low <= right:
            low+=1
        while p < A[high] and high >= left:
            high-=1
        if low < high:
            A[low],A[high] = A[high], A[low]

    A[left], A[high] = A[high], A[left]

    return high

def QuickSort(A,left,right): # 퀵정렬에 핵심부분 알고리즘
    if(left<right):
        p = Partition(A,left,right)
        QuickSort(A,left,p-1)
        QuickSort(A,p+1,right)

A = [5,1,3,7,9,11,12]
QuickSort(A,0,len(A)-1)
print(A)
