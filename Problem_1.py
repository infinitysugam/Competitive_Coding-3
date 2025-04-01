# Pascal Triangle
# Time Complexity = O(n2)
# Space Complexity = O(n)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(0,numRows):
            temp_result = []
            for j in range(0,i+1):
                if j==0 or j==i:
                    temp_result.append(1)
                else:
                    temp_result.append(result[i-1][j-1]+result[i-1][j])
        
            result.append(temp_result)
        return result                

        

