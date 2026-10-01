class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        freq={}
        for word in strs:
            alpha=[0]*26
            for ch in word:
                index=ord(ch)-ord('a')
                alpha[index]+=1
            key=tuple(alpha)
            if key not in freq:
                freq[key]=[]
            freq[key].append(word)
        return list(freq.values())