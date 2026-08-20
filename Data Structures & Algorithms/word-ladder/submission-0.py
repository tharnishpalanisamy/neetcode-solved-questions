class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set() 
        wordList = set(wordList)
        self.res = 1 

        def bfs(word) :

            queue = deque([word]) 

            while queue :
                level = len(queue) 
                for _ in range(level) :
                    word = queue.popleft() 
                    if word == endWord :
                        return True 
                    for i in range(len(word) ) :
                        alphabets = 'abcdefghijklmnopqrstuvwxyz' 
                        for c in alphabets :
                            new = word[:i] + c + word[i+1:] 

                            if new in wordList and new not in visited:
                                queue.append(new) 
                                visited.add(new)  
                self.res += 1 
            return False 
        
        if bfs(beginWord) :
            return self.res 
        else:
            return 0 
