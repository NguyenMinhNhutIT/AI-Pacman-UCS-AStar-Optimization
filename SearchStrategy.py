from MapGame import MapGame
import os
import copy
import time

class SearchStrategy:
    def search(self, map_game: MapGame):
        actions = []
        total_cost = 0
        return actions, total_cost
    
    def is_goal_state(self, state, map_game): # Phương thức trả về True nếu Pacman đã ăn được một điểm mồi và ngược lại
        if state is not None:
            x, y = state
            return map_game.map[x][y] == '.'
        return False

    def find_nearest_goal_state(self, current_state, map_game): # Phương thức tìm điểm mồi gần nhất
        min_distance = float('inf')
        nearest_goal_state = None

        for i, row in enumerate(map_game.map):
            for j, value in enumerate(row):
                if value == '.':
                    distance = abs(current_state[0] - i) + abs(current_state[1] - j) # Công thức tính khoảng cách 2 điểm trong tọa độ (x,y)
                    if distance < min_distance:
                        min_distance = distance
                        nearest_goal_state = (i, j)

        return nearest_goal_state


    ''' Định nghĩa các Hàm để Visualize các actions của Pacman '''
    def apply_action(self, current_state, action):
        '''Cập nhật trạng thái dựa trên hành động. '''
        x, y = current_state
        if action == 'North':  # Di chuyển lên
            return (x-1, y)
        elif action == 'South':  # Di chuyển xuống
            return (x+1, y)
        elif action == 'West':  # Di chuyển sang trái
            return (x, y-1)
        elif action == 'East':  # Di chuyển sang phải
            return (x, y+1)
        return current_state

    def clear_screen(self): 
        ''' Phương thức dùng để xóa màn hình console '''
        os.system('cls' if os.name == 'nt' else 'clear')

    def visualize_pacman_movement(self, map_game, actions): 
        ''' Phương thức dùng để mô phỏng chuyển động của Pacman '''
        display_map = copy.deepcopy(map_game.original_map)
        current_state = map_game.get_start_state()

        for action in actions:
            self.clear_screen() # Clear screen console để dễ dàng quan sát Pacman di chuyển
            next_state = self.apply_action(current_state, action) # Dựa vào actions để lấy bước đi tiếp theo của P
            display_map[current_state[0]][current_state[1]] = ' ' # Cập nhật vị trí vưa đi qua của P là rỗng
            display_map[next_state[0]][next_state[1]] = 'P' # Chuyển P tới vị trí mới
            self.print_map(display_map)  # Phương thức này sẽ in bản đồ khi cập nhật bước đi của P
            current_state = next_state
            time.sleep(0.1)
            
    def print_map(self, map_to_print): # Phương thức in bản đồ hiện tại
        for row in map_to_print:
            print("".join(row))
        print()
    
    
