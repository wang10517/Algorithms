class Solution:
    def countAndSay(self, n: int) -> str:
        cur_str = '1'
        for i in range(1,n):
            prev = cur_str[0]
            count = 1
            repl_str = ""
            for j in range(1,len(cur_str)):
                if prev == cur_str[j]:
                    count = count + 1
                else:
                    repl_str = repl_str + str(count) + str(prev)
                    count = 1
                    prev = cur_str[j]
            repl_str = repl_str + str(count) + str(prev)
            cur_str = repl_str
        return cur_str

print(Solution().countAndSay(4))