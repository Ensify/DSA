class Solution:

    def Merge(self,a,b,l):
        i=j=k=0
        while i<len(a) and j<len(b):
            if a[i]<b[j]:
                l[k]=a[i]
                i+=1
            else:
                l[k]=b[j]
                j+=1
            k+=1
        
        while i<len(a):
            l[k]=a[i]
            i+=1
            k+=1
        while j<len(b):
            l[k]=b[j]
            j+=1
            k+=1

    def MergeSort(self,l):
        if len(l)>1:
            mid=len(l)//2
            left  = l[:mid]
            right = l[mid:]
            self.MergeSort(left)
            self.MergeSort(right)
            self.Merge(left,right,l)

    def sortArray(self, nums: list[int]) -> list[int]:
        self.MergeSort(nums)
        return nums