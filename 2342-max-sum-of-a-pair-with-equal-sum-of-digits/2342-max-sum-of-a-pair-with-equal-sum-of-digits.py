import heapq

class Solution:

    def maximumSum(self, nums: list[int]) -> int:

        def digit_sum(n):
            if n < 10:
                return n
            return n % 10 + digit_sum(n // 10)

        freq = {}

        for num in nums:
            d = digit_sum(num)

            if d not in freq:
                freq[d] = []

            heapq.heappush(freq[d], num)

            if len(freq[d]) > 2:
                heapq.heappop(freq[d])

        ans = -1

        for key in freq:
            if len(freq[key]) == 2:
                total = freq[key][0] + freq[key][1]
                ans = max(ans, total)

        return ans