class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmax=nums[0]
        curmin=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            temp=curmax
            curmax=max(nums[i],nums[i]*curmax,nums[i]*curmin)
            curmin=min(nums[i],nums[i]*temp,nums[i]*curmin)
            ans=max(ans,curmax)
        return ans
