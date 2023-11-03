class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
       
                
        
        dic = {}
        sol = []
        for i in nums:
            if i not in dic:
                dic[i] = 0
        for i in nums:
            dic[i] += 1
        print(dic)
        for i in range(k):
            sol.append()
        return sol


x = Solution()
print(x.topKFrequent([1,2,3,4,5,6,7,8,1,2,3,4,5,6,1,2,3,4,5,1,2,3,1], 2))
