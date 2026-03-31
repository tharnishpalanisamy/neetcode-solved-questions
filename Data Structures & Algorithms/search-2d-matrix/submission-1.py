class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:   
        array = []
        for arr in matrix :
            if arr[-1] < target:
                continue
            elif arr[-1] >= target :
                array = arr 
                break
        l,r = 0 , len(array) - 1
        while l<= r:
            mid = (l+r)//2
            if array[mid] < target :
                l = mid + 1
            elif array[mid] > target:
                r = mid-1
            else:
                return True
        return False

