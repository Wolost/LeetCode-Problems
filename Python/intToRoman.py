class Solution:
    def intToRoman(self, num: int) -> str:
        mapn = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        mapl = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        i = 0
        numb = ""
        while i < len(mapn):
            if(num==0):break
            if(num >= mapn[i]):
                numb += mapl[i]
                num -= mapn[i]
            else:
                i += 1
        return numb

solution = Solution()

result = solution.intToRoman(3749)

print("Resultado: ",result)