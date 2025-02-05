class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen =set()
        for i in range(9):
            for j in range(9):
                b = board[i][j]
                if b == ".":
                    continue
                if (b + '@row ' + str(i) in seen or
                    b + '@col ' + str(j) in seen or
                    b + '@box ' + str(i // 3) + str(j // 3) in seen):
                    return False
                seen.add(b + '@row ' + str(i))
                seen.add(b + '@col ' + str(j))
                seen.add(b + '@box ' + str(i // 3) + str(j // 3))
        return True
        