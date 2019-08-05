class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        start, end = 0, len(A)-1
        arr = []
        while start <= end:
            startSquare = A[start]**2
            endSquare = A[end]**2
            if startSquare > endSquare:
                arr.insert(0,startSquare)
                start += 1
            else:
                arr.insert(0,endSquare)
                end -= 1
        return arr;