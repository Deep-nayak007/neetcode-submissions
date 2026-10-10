class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = 0
        for i in digits:
            n = n * 10 + i
        m = n + 1

        x = [int(char) for char in str(m)]
        return x     
        