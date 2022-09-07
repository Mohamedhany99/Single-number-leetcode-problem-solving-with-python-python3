class Solution(object):
    def singleNumber(self, nums):
        newlist = []
        duplist = []
        for i in nums:
            if i not in newlist:
                newlist.append(i)
            else:
                duplist.append(i)
        for i in range(0,len(newlist)):
            if newlist[i] not in duplist:
                result = newlist[i]
        return result
        
        """
        :type nums: List[int]
        :rtype: int
        """
        