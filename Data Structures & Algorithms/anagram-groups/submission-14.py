class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {} 
        for word in strs :
            count = [0] * 26  
            for l in word :
                key = ord(l) - 97 
                count[key] += 1
            count = tuple(count) 
            if count not in seen:
                seen[count] = [] 
            seen[count].append(word) 
        return list(seen.values())