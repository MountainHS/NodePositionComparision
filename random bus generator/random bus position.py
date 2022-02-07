from random import random
import pandas as pd
import math
import random
from tqdm import tqdm

def get_bus_data(path):  
    # bus 데이터 읽기
    bus_data = pd.read_csv(path)
    print("get bus data", bus_data, "\n", "*"*10)
    
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
    bus_coordinate.to_json("./random bus generator/result/random bus position.json")



if __name__ == '__main__':
    get_bus_data("./random bus generator/data/Bus_data_118bus.csv")          