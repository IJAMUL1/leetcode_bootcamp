class Solution(object):
    def videoStitching(self, clips, time):
        """
        :type clips: List[List[int]]
        :type time: int
        :rtype: int
        """
        can_cover = False
    
        # Check if at least one clip can cover the entire duration T
        for clip in clips:
            if clip[1] >= time:
                can_cover = True
                break
        
        if not can_cover:
            return -1
        
        start, s = 0, 0
        
        while start < time:
            max_end, index = -1, -1
            
            # Find the clip with the maximum end time that starts before or at the current start time
            for i, clip in enumerate(clips):
                if clip[0] <= start and max_end < clip[1]:
                    max_end = clip[1]
                    index = i
            
            if index == -1:
                return -1
            
            start = clips[index][1]
            s += 1
        
        return s
            