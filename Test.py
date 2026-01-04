from MapGame import MapGame
from Astar import Astar
from UCS import UCS
import os

def run_algorithm():
    map_folder = 'Sample_input'  # Đặt tên thư mục chứa tập tin bản đồ
    map_file = os.path.join(map_folder, input("Enter map-file: ")) # Nhập input tên bản đồ cần chạy
    chosen_algorithm = input("Enter algorithm type ('A*' or 'UCS'): ") # Nhập input tên thuật toán muốn tìm kiếm
    map_pacman = MapGame(map_file)
    if chosen_algorithm == 'A*':
        algorithm = Astar()
    elif chosen_algorithm == 'UCS':
        algorithm = UCS()
    else:
        print("Invalid algorithm type. Please enter 'A*' or 'UCS'.")
        return
    
    actions, total_cost = algorithm.search(map_pacman) # Thực hiện chiến lược tìm kiếm
    algorithm.visualize_pacman_movement(map_pacman, actions) # Thực hiện visualize từng action của Pacman
    print("Actions:", actions)
    print("Total Cost:", total_cost)

# main
run_algorithm()
