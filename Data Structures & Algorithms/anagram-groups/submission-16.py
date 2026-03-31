class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {} 
        for word in strs:
            count = [0] * 26 
            for c in word :
                key = ord(c) - 97 
                count[key] += 1 
            if not tuple(count) in group : 
                group[tuple(count)] = [] 
            group[tuple(count)].append(word) 
        return list(group.values())