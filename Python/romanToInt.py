class Solution:
    def romanToInt(self, s: str) -> int:
        num_map = {
            "I":1,
            "V":5,    "IV":4,
            "X":10,   "IX":9,
            "L":50,   "XL":40,
            "C":100,  "XC":90,
            "D":500,  "CD":400,
            "M":1000, "CM":900,
        }
        a = list(s)
        r = 0
        
        while len(a) != 0:
            if( len(a) > 1 and a[0]+a[1] in num_map):
                r += num_map[a[0]+a[1]]
                del a[0]
                del a[0]
            else:
                r += num_map[a[0]]
                del a[0]   
        return r

solution = Solution()

result = solution.romanToInt("MCMXCIV")

print("Resultado: ",result)