from SearchStrategy import SearchStrategy
from MapGame import MapGame
from queue import PriorityQueue

class UCS(SearchStrategy):
    def search(self, map_game: MapGame):
        '''' Cài đặt thuật toán BFS để tìm đường tất cả các điểm mồi có trong MapGame '''
        start_state = map_game.get_start_state() # Lấy vị trí của Pacman
        frontier = PriorityQueue()
        frontier.put((0, start_state, []))  # (cost, state, actions)
        explored = set()
        
        while not frontier.empty():
            cost, current_state, actions = frontier.get()
            explored.add(current_state)
            
            if self.find_nearest_goal_state(current_state, map_game) is None: # Không còn điểm mồi nào trên bản đồ
                actions.append('Stop')
                return actions, cost
            
            if self.is_goal_state(current_state, map_game):
                map_game.update_map(current_state)  # Cập nhật bản đồ khi đạt được mục tiêu
                frontier = PriorityQueue()
                frontier.put((cost, current_state, actions))  # Reset frontier với cost, current state, actions
                explored = set() # Reset lại explored
         
            successors = map_game.get_successors(current_state)
            for next_state, direction, step_cost in successors:
                if next_state not in explored: # Kiểm tra next_state đã explored hay chưa
                    state_in_frontier = any(item[1] == next_state for item in frontier.queue)
                    if not state_in_frontier: # Kiểm tra next_state có trong frontier không
                        new_cost = cost + step_cost  # step_cost luôn bằng 1
                        new_actions = actions + [direction]  # Thêm action của next_state vào list actions
                        frontier.put((new_cost, next_state, new_actions)) # Put dữ liệu vào frontier

        return [], 0
    