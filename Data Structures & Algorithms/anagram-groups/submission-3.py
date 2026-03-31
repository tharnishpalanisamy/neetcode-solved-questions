class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for l in word:
                count[ord(l) - ord("a")] += 1
            seen[tuple(count)].append(word)
        return list(seen.values())
        