class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "" :
            return []
        digitsToChar = {
            "2":"abc" , "3":"def" , "4":"ghi" , 
            "5":"jkl" , "6" : "mno" , "7" : "pqrs" , 
            "8":"tuv" , "9" : "wxyz"
        }
        res = [] 

        def backtrack(index , path):
            if len(path) == len(digits) :
                res.append(path[:])
                return
            chars = digitsToChar[digits[index]]
            for c in chars :  
                backtrack(index+1,path + c )
        backtrack(0,"")
        return res
                