class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Preprocesar la cadena para manejar palíndromos de longitud impar y par
        T = '#'.join(f'^{s}$')  # Agregar un separador y delimitadores
        n = len(T)
        
        # Inicializar el arreglo de longitudes de palíndromos
        P = [0] * n  # Longitud de palíndromos centrados en cada posición
        C = 0  # Centro del palíndromo más largo encontrado
        R = 0  # Límite derecho del palíndromo más largo encontrado
        max_length = 0  # Longitud máxima del palíndromo encontrado
        center_index = 0  # Índice central del palíndromo más largo en la cadena transformada T

        for i in range(1, n - 1):  # Iterar sobre la cadena transformada
            # Encuentra el espejo de i respecto al centro C
            i_mirror = 2 * C - i
            
            # Si i está dentro del rango de R, usa el valor del espejo para inicializar P[i]
            if i < R:
                P[i] = min(R - i, P[i_mirror])
            
            # Expandir el palíndromo centrado en i
            while T[i + P[i] + 1] == T[i - P[i] - 1]:
                P[i] += 1
            
            # Actualizar C y R si el palíndromo expandido supera el límite derecho
            if i + P[i] > R:
                C = i
                R = i + P[i]
            
            # Actualizar el palíndromo más largo encontrado
            if P[i] > max_length:
                max_length = P[i]
                center_index = i

        # Calcular el inicio de la subcadena palindrómica en la cadena original `s`
        start = (center_index - max_length) // 2  # Convertir índice de T a índice de `s`
        
        # Retornar el palíndromo más largo extraído de `s`
        return s[start: start + max_length]

solution = Solution()

result = solution.longestPalindrome("babad")

print("Resultado: ",result)