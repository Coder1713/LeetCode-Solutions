class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        ans=nums[0]
        for i in range(len(nums)):
            if(count==0):
                ans=nums[i]
            if(ans==nums[i]):
                count+=1
            else:
                count-=1
        if(nums.count(ans)>(len(nums)//2)):
            return ans
        else:
            return None


