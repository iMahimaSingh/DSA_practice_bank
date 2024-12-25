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

Question 2:-#  Given a signed 32-bit integer x, return the integer with its digits reversed.
# the integer causes the value to go outside the signed 32-bit integer 
# range [-2^31, 2^31 - 1], then return 0.
class Solution:
    def reverse(self, x: int) -> int:
        str_x=str(x)
        negative_number=x<0
        if str_x[0]=="-":
            reversed_number="-"+str_x[:0:-1]
        else:
            reversed_number=str_x[::-1]
        int_reversed_number=int(reversed_number)
        if int_reversed_number<-2**31 or int_reversed_number>2**31-1:
            return 0
        return int_reversed_number        
Qusetion 3:-
#  Given a positive integer n, count how many of its digits divide n evenly.
#  A digit d divides n evenly if n % d == 0.

#  Digits of n should be checked individually.
#  If a digit is 0, it should be ignored because division by 0 is undefined.
#  Return the total number of digits of n that divide n evenly.
class Solution:
    def evenlyDivides(self, n):
        # code here
        count=0
        for digits in str(n):
            int_digits=int(digits)
            if int_digits!=0 and n%int_digits==0:
                 count+=1
        return count    

# Selection sort
class Solution: 
    def selectionSort(self, arr):
        n=len(arr)
        for i in range(n-1):
            min_index=i
            for j in range(i,n):
                if(arr[j]<arr[min_index]):
                    min_index=j
            arr[i] ,arr[min_index]=arr[min_index],arr[i]  
        return arr

# Bubble sort
class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr):
        n=len(arr)
        for i in range(n-1,0,-1):
            
            for j in range(0,i):
                if(arr[j]>arr[j+1]):
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr  

# Insertion sort    

class Solution:
    def insertionSort(self, arr):
        n=len(arr)
        for i in range(1,n):
            j=i
            while (j>0  and arr[j-1]>arr[j]):
                arr[j-1],arr[j]=arr[j],arr[j-1]
                j-=1
        return arr  


# Merge sort    
class Solution:

    def mergeSort(self, arr, l, r):
        if l < r:
            # Find the middle point
            mid = (l + r) // 2
            
            # Recursively sort the first and second halves
            self.mergeSort(arr, l, mid)
            self.mergeSort(arr, mid + 1, r)
            
            # Merge the sorted halves
            self.merge(arr, l, mid, r)

    def merge(self, arr, l, mid, r):
        # Sizes of the two subarrays
        n1 = mid - l + 1
        n2 = r - mid
        
        # Create temp arrays
        left = [0] * n1
        right = [0] * n2
        
        # Copy data to temp arrays
        for i in range(0, n1):
            left[i] = arr[l + i]
        for j in range(0, n2):
            right[j] = arr[mid + 1 + j]
        
        # Merge the temp arrays back into arr[l..r]
        i = 0  # Initial index of the first subarray
        j = 0  # Initial index of the second subarray
        k = l  # Initial index of the merged subarray
        
        while i < n1 and j < n2:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        # Copy the remaining elements of left[], if any
        while i < n1:
            arr[k] = left[i]
            i += 1
            k += 1
        
        # Copy the remaining elements of right[], if any
        while j < n2:
            arr[k] = right[j]
            j += 1
            k += 1

# Example Usage
arr = [12, 11, 13, 5, 6, 7]
solution = Solution()
solution.mergeSort(arr, 0, len(arr) - 1)

#Quick sort

class Solution:
    # Function to sort a list using quick sort algorithm.
    def quickSort(self, arr, low, high):
        if low < high:
            # Partition the array and get the pivot index
            pi = self.partition(arr, low, high)

            # Recursively sort elements before and after partition
            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)

    # Function to partition the array and return the pivot index.
    def partition(self, arr, low, high):
        # Pivot is the last element
        pivot = arr[high]
        i = low - 1  # Index for the smaller element

        for j in range(low, high):
            # If the current element is less than or equal to the pivot
            if arr[j] <= pivot:
                i += 1  # Increment index for the smaller element
                arr[i], arr[j] = arr[j], arr[i]  # Swap elements

        # Swap the pivot element with the element at i+1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

# Example Usage
if __name__ == "__main__":
    arr = [4, 1, 3, 9, 7]
    solution = Solution()
    solution.quickSort(arr, 0, len(arr) - 1)
    


