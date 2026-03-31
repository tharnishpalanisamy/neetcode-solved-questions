class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            counts = [0] * 26
            for letter in word:
                counts[ord(letter) - 97] += 1
            result[tuple(counts)].append(word)
        return list(result.values())
