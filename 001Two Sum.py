class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #define i as the index 
        i_i = 0
        for i in nums:
            lookup_ = target -i
            #define k as the index for another round
            k_i = 0
            for k in nums:
                if k == lookup_:
                    if k_i == i_i:
                        #do nothing
                        #return [k_i,i_i]
                        pass
                    else:
                        #print nums[i_i]
                        return [i_i,k_i]
                k_i = k_i+1
            i_i = i_i+1
