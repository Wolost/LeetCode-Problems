from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_map = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        
        if len(digits) not in range(1, 5):
            return []
               
        combinations = [""]
        
        for digit in digits:
            letters = letter_map[int(digit) - 2]

            combinations = [prefix + letter for prefix in combinations for letter in letters]
        
        return combinations

solution = Solution()

result = solution.letterCombinations("234")

print("Resultado: ",result)