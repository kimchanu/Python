def Merge(left,right): # 두값 합침.
    v=[]
    i=0
    j=0    # 오른쪽 왼쪽 한값씩 비교하면서 정렬하기 위해
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            v.append(left[i])
            i=i+1
        else:
            v.append(right[j])
            j=j+1
    while i<len(left):
        v.append(left[i])
        i+=1
    while j<len(right):
        v.append(right[j])
        j+=1
    return v

def MergeSort(A):
    if len(A) <=1:
        return A
    mid = len(A)//2
    left1 = A[:mid] # 배열을 반으로 나눔
    right1 = A[mid:]
    L1 = MergeSort(left1) # 후위순회
    R1 = MergeSort(right1)
    return Merge(L1,R1)

A1 = [37,10,22,30,35,13,25,24]
print(MergeSort(A1))

Recursion  Reference : https://velog.io/@polynomeer/%EC%9E%AC%EA%B7%80Recursion
