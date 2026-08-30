class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix=0
        mp={0:1}
        count=0
        for i in range(len(nums)):
            prefix=prefix+nums[i]
            if prefix-k in mp:
                count=count+mp[prefix-k]
            mp[prefix]=mp.get(prefix,0)+1
        return count
        