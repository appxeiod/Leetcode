class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #buffer stores the non repeating characters
        buffer = ""
        #buffer index
        k = 0
        p = 1
        #repeat flag
        buffer_flag = 0
        #maximum string
        max_index = 0
        
        for i in s:
            #print "in s:"+i
            #print "now buffer:"+buffer
            p = 1
            for j in buffer:
                if i == j:
                    buffer_flag = 1
                    break
                else:
                    buffer_flag = 0
                    p=p+1
            if buffer_flag == 1:
                k= k-p+1
                #del buffer
                buffer += i
                #print "buffer:"+buffer
                buffer = buffer[p:]
                #print "buffer:"+buffer
                buffer_flag = 0
            else :
                buffer+= i
                k = k+1
            if k >=max_index:
                max_index = k
            #print "buffer:"+buffer
            #print "now in k:",k
            #print "now in max_index:",max_index
        
        return max_index 
                    