class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = sorted(zip(position,speed), reverse=True)
        stack=[]

        for position,speed in pair:
            time = (target-position)/speed
            if not stack or time>stack[-1]:
                stack.append(time)
        return len(stack)        