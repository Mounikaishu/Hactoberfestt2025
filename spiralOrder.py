class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        if not matrix:
            return res

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # left → right
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1

            # top → bottom
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            # right → left
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1

            # bottom → top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res
