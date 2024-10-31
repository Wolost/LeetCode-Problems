class Solution:
    def convert(self, s: str, numRows: int) -> str:
        index, direction = 0, 0
        rows = [ [] for _ in range(numRows)]
        
        for char in s:
            rows[index].append(char)
            if index == 0 and numRows > 1:
                direction = 1
            elif index == numRows-1 and numRows > 1:
                direction = -1
            index += direction
            
        rows_str = ''.join(map(str, sum(rows, [])))
        return(rows_str)
            
    
solution = Solution()

result = solution.convert("ABC", 1 )

print("Resultado: ",result)