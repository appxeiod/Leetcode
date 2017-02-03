class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #counting index
        k = 0
        #output indices
        out1 = 0
        out2 = 0
        for i in nums1:
            k += 1
        for j in nums2:
            k += 1
            
        #offset isusse!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        
        #test line    
        #print k
        
        if k%2 == 0:
            k = k/2
            out1 = k-1
            out2 = k
        else:
            k = k/2
            out1 = k
            out2 = k
        
        #test line
        #print k,out1,out2
        
        #buffer_index 
        buffer_index = 0
        #buffer indices
        buffer_i = 0
        buffer_j = 0
        #buffer hand indices
        hand_i = 0
        hand_j = 0
        #comparasion buffer
        buffer = {}
        
        while buffer_index <= out2:
            #test line
            #print buffer_i,buffer_j,buffer
            #print buffer_index
            
            try:#nums1[buffer_i] != 'null':
                try:#nums2[buffer_j] != 'null':
                    #print "both"
                    if nums1[buffer_i] >= nums2[buffer_j]:
                        buffer[buffer_index] = nums2[buffer_j]
                        buffer_j += 1
                        buffer_index += 1
                    else: 
                        buffer[buffer_index] = nums1[buffer_i]
                        buffer_i += 1
                        buffer_index += 1
                except:
                    #print "10"
                    buffer[buffer_index] = nums1[buffer_i]
                    buffer_i += 1
                    buffer_index += 1
            except:
                try:# nums2[buffer_j] != 'null':
                    #print "01"
                    buffer[buffer_index] = nums2[buffer_j]
                    buffer_j += 1
                    buffer_index += 1
                except:
                    #print "00"
                    #should never reaches here
                    #print "error"
                    #break
                    pass
        
        #test line
        #print buffer[out1],buffer[out2]
        #print buffer_index
        #print buffer
        
        output = buffer[out1]+buffer[out2]
        output = float(output)
        output = output/2
        
        return output
            
        