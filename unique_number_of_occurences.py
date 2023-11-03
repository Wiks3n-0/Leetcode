class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        # hashmap to store numbers of an array as keys and number of occurences as values
        dic = {}
        for i in arr:
            if i not in dic.keys():
                dic[i] = 0
        # adding 1 for each occurence of a number in an array
        for i in arr:
            dic[i] += 1
        values = dic.values()
        # initializing hashset so we can store number of occurences
        hset = {-1}
        # copying values from hashmap simultanously checking if they already exist,
        # if so False is returned, if thru all of the loop there is no duplicate True
        for i in values:
            if i in hset:
                return False
            else:
                hset.add(i)
        return True

x = Solution()

print(x.uniqueOccurrences([1,2,2,3,3,3,1]))
