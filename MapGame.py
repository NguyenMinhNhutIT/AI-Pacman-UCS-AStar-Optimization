from queue import PriorityQueue
import time
import os
import math
import copy

class MapGame:
    def __init__(self, map_file):
        self.load_map(map_file)
        self.add_dots_to_corners() # Thêm 4 dot vào 4 góc tường để Pacman đi đủ 4 góc

    def load_map(self, map_file):
        with open(map_file, 'r') as file:
            # Lưu map gốc để dùng cho việc Visualize
            self.original_map = [list(line.strip()) for line in file.readlines()]
        # Tạo biến map để xử lý trên biến map này
        self.map = copy.deepcopy(self.original_map)

    def get_successors(self, state):
        x, y = state
        successors = []

        # Định nghĩa các hướng đi cho Pacman
        movements = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        directions = ['North', 'East', 'South', 'West']

        for i, (nx, ny) in enumerate(movements):
            if 0 <= nx < len(self.map) and 0 <= ny < len(self.map[0]) and self.map[nx][ny] != '%':
                successors.append(((nx, ny), directions[i], 1))  # (next_state, action, step_cost) với step_cost luôn bằng 1

        return successors

    def add_dots_to_corners(self):
        # Thêm điểm mồi góc trên bên trái
        if self.map[1][1] != 'P' and self.map[1][1] != '%':
            self.map[1][1] = '.'
        # Thêm điểm mồi góc trên bên phải
        if self.map[1][-2] != 'P' and self.map[1][-2] != '%':
            self.map[1][-2] = '.'
        # Thêm điểm mồi góc dưới bên trái
        if self.map[-2][1] != 'P' and self.map[-2][1] != '%':
            self.map[-2][1] = '.'
        # Thêm điểm mồi góc dưới bên phải
        if self.map[-2][-2] != 'P' and self.map[-2][-2] != '%':
            self.map[-2][-2] = '.'

    def update_map(self, state): # Phương thức sẽ xóa điểm mồi  sau khi Pacman đã ăn
        x, y = state
        if self.map[x][y] == '.':  
            self.map[x][y] = ' '

    def get_start_state(self): # Lấy vị trí ban đầu của Pacman
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                if self.map[i][j] == 'P':
                    return (i, j)
        