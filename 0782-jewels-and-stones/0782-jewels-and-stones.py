class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = {} # dictionary
        aux = 0 #iterates through jewels to see how many of th stones are jewels
        for letter in stones:
            count[letter] = count.get(letter,0) + 1 #iterating through each stone to get the current count of the stones starting  with 0 by default and then incrementing it 
        for jewel in jewels:
            aux+=count.get(jewel,0) #after iterating through each character in jewels, it checks how many appeared in the stones
        return aux # returns the final count of jewels 