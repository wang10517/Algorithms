# Analysis:
#     how to compile the rules into the code?
#     1. the number of a certain charcater matters
#     2. the position of that number also matters in the context
#     3. you could have the letter of the same precedence not continuous to each other
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

lookup = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C'  : 100, 
            'D'  : 500,
            'M' : 1000
        }


class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        dire = ''
        while s:
            returns = self.pop(s)
            if not result:
                result = returns[1]
            else:
                if dire == '+':
                    result = result + returns[1]
                else:
                    result = result - returns[1]
            dire = returns[2]
            s = returns[0]
        return result
    
    def pop(self, s: str):
        keys = list(lookup.keys())
        lens = len(keys)
        for i in range(len(keys)):
            if keys[lens - 1 - i] in s:
                key = keys[lens - 1 - i]
                value = lookup[key]
                dire = '+'
                if s.index(key) > 0:
                    dire = '-'
                s = s.replace(key, '', 1)
                return [s, value ,dire]
## After the run, this solution seems to be very slow but memory efficient

## A much better pyhton solution:
# class Solution(object):
	# def romanToInt(self, s):
	# 	dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
	# 	prev = None
	# 	count = 0
	# 	for i in range(len(s)-1,-1,-1):
	# 		curr = s[i]
	# 		if prev is not None and dic[prev] > dic[curr]:
	# 			count-=dic[curr]
	# 		else:
	# 			count+=dic[curr]
	# 		prev = curr
		
	# 	return count  
# it turns out there is no need for recursion, iteration would do the work 
# since you only need to store the information of the previous digits
            

        