class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = []
        count = 1
        x = sorted(nums)
        for i in range(len(nums) - 1):
            if(x[i] == x[i+1]):
                count = count + 1
            else:
                counts.append([count, x[i]])
                count = 1
        counts.append([count, x[-1]])
        counts.sort(reverse = True)
        output = []
        for i in range(k):
            output.append(counts[i][1])
                
        return output            

        