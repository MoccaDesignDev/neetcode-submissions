# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs)-1)

    def mergeSortHelper(self, pairs: List[Pair], s:int, e:int)-> List[Pair]:
        if e - s + 1 <= 1:
            return pairs
        
        #the middle index of the array
        m = (s + e)//2

        #sort the left half
        self.mergeSortHelper(pairs, s, m)

        #sort the rigth half
        self.mergeSortHelper(pairs, m + 1, e)

        #merge sorted half
        self.merge(pairs, s, m ,e)

        return pairs


    #merge in-place
    def merge(self, arr: List[Pair], s:int, m:int, e:int)-> None:
        #copy the sorted left & right halfs to the temp arrya
        L = arr[s:m+1]
        R = arr[m+1 :e+1]

        i = 0 #setting index for L
        j = 0 #setting index for right
        k = s # setting index for arr

        #merge the two sorted halfs into the original array
        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j +=1
            k+=1
        # one of the halfs will have element remaining
        while i < len(L):
            arr[k] = L[i]
            i +=1
            k +=1
        while j <len(R):
            arr[k] = R[j]
            j +=1
            k +=1