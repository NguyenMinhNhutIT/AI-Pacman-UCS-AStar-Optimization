from SearchStrategy import SearchStrategy
from MapGame import MapGame
from queue import PriorityQueue

class Astar(SearchStrategy):
    ''' Cài đặt hàm Heuristic cho A* '''
    def manhattan_distance(self, state, map_game):
        # Tìm dot gần nhất
        goal_state = self.find_nearest_goal_state(state, map_game)

        if goal_state is None:
            return 0

        # Tính khoảng cách Manhattan từ trạng thái hiện tại đến node dot gần nhất
        return abs(state[0] - goal_state[0]) + abs(state[1] - goal_state[1]) # Bằng tổng độ lệch cột và đột lệch hàng so với dot


    def search(self, map_game: MapGame):
        '''' Cài đặt thuật toán A* để tìm đường đi với hàm manhattan_distance là hàm h(n) '''
        start_state = map_game.get_start_state() # Lấy start state của bài toán từ phương thức get_start_state()        
        frontier = PriorityQueue() # Khởi tạo frontier để lưu các node đang xét với hàng đợi ưu tiên 
        frontier.put((0 + self.manhattan_distance(start_state, map_game), 0, start_state, []))  # (fn, total cost, state, actions)
        explored = set() # Khởi tạo tập hợp explored
        
        while not frontier.empty(): # Lặp đến khi frontier rỗng
            estimated_total_cost, total_cost, current_state, actions = frontier.get()
            explored.add(current_state)
            goal_state = self.find_nearest_goal_state(current_state, map_game)
            
            if goal_state is None:  # Pacman đã ăn hết điểm mồi
                actions.append('Stop')
                return actions, total_cost
            
            if self.is_goal_state(current_state, map_game):
                map_game.update_map(current_state)  # Cập nhật bản đồ khi đạt được mục tiêu
                frontier = PriorityQueue()
                frontier.put((self.manhattan_distance(current_state, map_game), total_cost, current_state, actions))  # Reset frontier và put (h(current_state), total cost, current_state, actions)
                explored = set() # Reset set explored
                
            for next_state, direction, step_cost in map_game.get_successors(current_state):
                if next_state not in explored: # Kiểm tra next_state đã explored hay chưa
                    state_in_frontier = any(item[2] == next_state for item in frontier.queue)
                    if not state_in_frontier: # Kiểm tra next_state có trong frontier không
                        new_cost = total_cost + step_cost # Tính gn' = gn + 1
                        new_actions = actions + [direction] # Thêm action của next_state vào list actions
                        estimated_total_cost = new_cost + self.manhattan_distance(next_state, map_game) # fn = gn' + h(next_state)
                        frontier.put((estimated_total_cost, new_cost, next_state, new_actions)) # Put dữ liệu vào frontier

        return [], 0

