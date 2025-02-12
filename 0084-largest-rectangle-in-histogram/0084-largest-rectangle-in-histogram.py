class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        stack=[(0,heights[0])]
        max_histogram=0
        for i in range(1,n):
            if heights[i]>=stack[-1][1]:
                stack.append((i,heights[i]))
            else:
                while stack and stack[-1][1]>heights[i]:
                    index,h=stack.pop()
                    max_histogram=max(max_histogram,(i-index)*h)
                else:
                    stack.append((index,heights[i]))
        index_new=len(heights) 
        while stack:
            index,h=stack.pop()
            max_histogram=max(max_histogram,(index_new-index)*h)
        return max_histogram