class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]  
        max_area = 0  

        for i, h in enumerate(heights):
            while len(stack) > 1 and heights[stack[-1]] > h:  
                top = stack.pop()  
                width = i - stack[-1] - 1 if len(stack) > 1 else i  
                max_area = max(max_area, heights[top] * width)  

            stack.append(i)  

        while len(stack) > 1:  
            top = stack.pop()
            width = len(heights) - stack[-1] - 1 if len(stack) > 1 else len(heights)
            max_area = max(max_area, heights[top] * width)  

        return max_area


            