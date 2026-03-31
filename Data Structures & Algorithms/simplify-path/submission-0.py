class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = [] 
        cur = ""  #"/neetcode/practice//...///../courses"
        for c in path + "/" : #"/neetcode/practice//...//courses"
            if c == "/" :  #"/neetcode/practice/courses"
                if cur == ".." :
                    if stack : stack.pop() 
                elif cur != "" and cur != "." :
                    stack.append(cur) 
                cur = ""
            else:
                cur += c
        return "/"+"/".join(stack)