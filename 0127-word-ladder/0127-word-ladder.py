class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset=set(wordList)
        if endWord not in wordset:
            return 0
        q=deque()
        visited=set()
        q.append((beginWord,1))
        while q:
            word,level=q.popleft()
            if word==endWord:
                return level
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    newWord=word[:i]+ch+word[i+1:]
                    if newWord in wordset and newWord not in visited:
                        q.append((newWord,level+1))
                        visited.add(newWord)
        return 0
                
        
    