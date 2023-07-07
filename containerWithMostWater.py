class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        mxarea = 0 
        while(i < j):
            if(height[i]<height[j]):
                area = height[i]*(j-i)
                i+=1
            else:
                area = height[j]*(j-i)
                j-=1
                
            if mxarea < area:
                mxarea = area
        
        return mxarea
            
