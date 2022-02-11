import os
import pandas as pd
import math
import random
import matplotlib.pyplot as plt

ROOT = os.getcwd()
DATA = "/random bus generator/" + "data/"
RESULT = "/random bus generator/" + "result/"
BUS = "bus-1062"
BRANCH = "branch-1062"

CSV = ".csv"
JSON = ".json"

BUS_PATH = ROOT + DATA + BUS + CSV
BRANCH_PATH = ROOT + DATA + BRANCH + CSV


def make_random_bus_position(path):  
    # bus 데이터 읽기
    bus_data = pd.read_csv(path)
    print("get bus data", bus_data, "*"*10, end="\n")
    
    # bus 개수 가져오기
    row_count = len(bus_data.index)
    print("bus data row count", row_count, type(row_count), "\n", "*"*10)
    
    additional_width = 0.1

    # bus 들이 들어갈 그리드셀 너비
    square_width = round(math.sqrt(row_count))
    
    # bus들 리스트 만들고 섞기
    bus_id = list(range(1,row_count+1))
    random.shuffle(bus_id)
    print("shuffled bus id list:", bus_id, "\n", "*"*10)
    bus_coordinate = []
    
    # 섞은 bus들에 좌표 붙이기
    count = 0
    for i in range(square_width):
        for j in range(square_width):
            bus_coordinate.append({"bus id": bus_id[count], "x": i, "y": j})
            count += 1
            
            if (count == row_count):
                break
            
        if (count == row_count):
            break
        
    # json 형태로 출력
    bus_coordinate = sorted(bus_coordinate, key = lambda x:(x['bus id']))
    bus_coordinate = pd.DataFrame(bus_coordinate)
    print(bus_coordinate, "\n", "*"*10)
    bus_coordinate.to_json(ROOT + RESULT + BUS + " random position" + JSON)
    
def get_bus_degree(path):
    # branch 데이터 읽기
    branch_data = pd.read_csv(path)
    print("get branch data", branch_data, "*"*10, end="\n")
    
    # branch 개수 가져오기
    row_count = len(branch_data.index)
    print("branch data row count", row_count, type(row_count), "\n", "*"*10)
    
    # connected_bus: 각 bus간 연결된 bus들을 리스트로 저장
    connected_bus = []
    for i in range(1062):
        connected_bus.append([])
    print("connected_bus list initialize...")
    print(connected_bus, "\n", "*"*10)
        
    for i in range(row_count):
        try:
            start_bus = branch_data.iloc[i, 0] - 1
            end_bus = branch_data.iloc[i, 1] - 1
            
            connected_bus[start_bus].append(end_bus)
            connected_bus[end_bus].append(start_bus)
            
        except IndexError:
            print("IndexError!", start_bus, end_bus)
            
    print("connected_bus list result")
    print(connected_bus, "\n", "*"*10)
        
    # result: connected_bus를 통해 bus간 connected_bus 값 가져오기
    result = []
    for i in range(1062):
        result.append({"bus id": i + 1, "connected_bus": len(connected_bus[i])})
    result = pd.DataFrame(result)
    print("connected_bus dataframe")
    print(result, "\n", "*"*10)
    
    # result를 히스토그램 형태로 표현
    result["connected_bus"].plot(kind="hist")
    plt.show()
    
    result.to_json(ROOT + RESULT + BUS + " connected_bus" + JSON)
    

if __name__ == '__main__':
    # print(BUS_PATH)
    # make_random_bus_position(BUS_PATH)
    print(BRANCH_PATH)
    get_bus_degree(BRANCH_PATH)          