

def get_data_in_rows() -> tuple[list[str], list[str], list[str]]:
    with open('project/data.txt', 'r', encoding='utf-8') as f:
        data = f.read().strip().split('\n')

    data1 = []
    data2 = []
    data3 = []
    
    for i in range(0, len(data), 3):
        data1.append(data[i])
        if i + 1 < len(data):
            data2.append(data[i + 1])
        if i + 2 < len(data):
            data3.append(data[i + 2])
        
        
    return (data1, data2, data3)
