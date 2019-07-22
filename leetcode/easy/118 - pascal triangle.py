class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = []
        if not numRows:
            return []

        prev_row = [] 
        for row in range(0,numRows):
            cur_row = [1]
            if prev_row:
                for i in range(1,len(prev_row)):
                    cur_row.append(prev_row[i-1] + prev_row[i])
                cur_row.append(1)
            tri.append(cur_row)
            prev_row = cur_row
                

        return tri
