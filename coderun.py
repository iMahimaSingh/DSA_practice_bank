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
