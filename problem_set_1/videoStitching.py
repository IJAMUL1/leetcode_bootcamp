class Solution(object):
    def videoStitching(self, clips, time):
        """
        :type clips: List[List[int]]
        :type time: int
        :rtype: int
        """
        total_time_covered,c_used,itr = 0,0,0
        saved =[0,0]
        prev =[0,0]
        while total_time_covered < time:
            if itr < len(clips):
                if clips[itr][0]<=saved[0] and clips[itr][1] > saved[1]:
                    saved = clips[itr]
                itr +=1
            
            # print(itr, len(clips))
            if itr==len(clips):
                itr =0
                total_time_covered +=saved[1] - prev[1]
                if saved[1] == prev[1]:
                    return -1
                prev =saved
                saved[0] = saved[1]
                c_used +=1 
            
        return c_used
        