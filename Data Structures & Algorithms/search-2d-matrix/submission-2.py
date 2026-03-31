class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        startr = 0 
        endr = len(matrix) - 1 
        while startr <= endr:
            row = (startr+endr)//2
            if target < matrix[row][0]:
                endr = row - 1 
            elif target > matrix[row][-1] :
                startr = row + 1 
            else:
                break
        if startr > endr:
            return False

        row = (startr + endr)//2
        l,r = 0 , len(matrix[0])  
        while l <= r :
            mid = (l+r)//2
            if target > matrix[row][mid] :
                l = mid + 1 
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        return False