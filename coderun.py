# largest element in the array
def largestElement(arr: [], n: int) -> int:
    if not arr:
        return float('-inf')
    largest_no=arr[0]
    for i in range(n):
        if(arr[i]>largest_no):
            largest_no=arr[i]
    return(largest_no)
arr=[4,7,8,6,7,6]
n=len(arr)    
(largestElement(arr,n))
