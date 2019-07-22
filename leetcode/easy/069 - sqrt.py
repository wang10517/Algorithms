class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        if x ==0:
            return 0
        start = 1
        end = int(x/2)
    
        while True:
            cur = int((start+end)/2) 
            est = cur**2
            if est  == x:
                return cur
            
            if est < x:
                if (cur+1)**2 > x:
                    return cur
                else:
                    start = cur+1
            else:
                if (cur+1)**2 < x:
                    return cur
                else:
                    end = cur - 1
            
            
                    
        