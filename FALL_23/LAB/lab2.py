# # import numpy as np

# # def walk_zigzag(floor):
# #     rows, cols = floor.shape
# #     walking_sequence = []

# #     for i in range(rows):
# #         if i % 2 == 0:
# #             for j in range(cols):
# #                 walking_sequence.append(floor[i, j])
# #         else:
# #             for j in range(cols - 1, -1, -1):
# #                 walking_sequence.append(floor[i, j])

# #     return walking_sequence

# # floor = np.array([['3', '8', '4', '6', '1'],
# #                   ['7', '2', '1', '9', '3'],
# #                   ['9', '0', '7', '5', '8'],
# #                   ['2', '1', '3', '4', '0'],
# #                   ['1', '4', '2', '8', '6']])

# # print('Walking sequence:')
# # sequence = walk_zigzag(floor)
# # for row in sequence:
# #     print(row)

# def wall_up(matrix, depth):
#     rows, cols = len(matrix), len(matrix[0])
#     new_rows = rows + 2 * depth
#     new_cols = cols + 2 * depth
#     new_matrix = [[8] * new_cols for _ in range(new_rows)]
#     for i in range(rows):
#         for j in range(cols):
#             new_matrix[i + depth][j + depth] = matrix[i][j]
#     return new_matrix
# array = [
#     [2, 3, 4],
#     [3, 4, 6],
#     [2, 1, 4]
# ]
# depth = 1
# x = wall_up(array, depth)
# for row in x:
#     print(row)
# #######################################3
import numpy as np

def calculate_strength_diff(clubroom):
    rows, cols = clubroom.shape
    size = (rows * cols) // 2
    strength_diff = np.zeros(size, dtype=int)
    diff_index = 0
    for i in range(rows):
        for j in range(cols):
            if i < j:
                strength_diff[diff_index] += clubroom[i, j]
            elif i > j:
                strength_diff[diff_index] -= clubroom[i, j]
                strength_diff[diff_index] = abs(strength_diff[diff_index])
                diff_index += 1
    return strength_diff

clubroom = np.array([[1, 2, 9, 7], [4, 5, 1,8], [3,6,2,7],[2,8,8,3]])
strength_diff = calculate_strength_diff(clubroom)
print(strength_diff)
