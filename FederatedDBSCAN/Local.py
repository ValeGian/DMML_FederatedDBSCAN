from scipy.io import arff
import numpy as np
import math

L = 0.01
PARTITIONS_PATH = "./partitions/partition"


def compute_local_update(my_index):
    #data, meta = arff.loadarff(f'{PARTITIONS_PATH}{my_index}.arff')
    data, meta = arff.loadarff('datasets/banana.arff')

    dimension = len(data[0]) - 1

    points = []

    for row in data:
        points.append(tuple(math.floor(row[i] / L) for i in range(dimension)))

    arr_points = np.array(points)

    max_x = np.amax(arr_points[:, 0])
    max_y = np.amax(arr_points[:, 1])

    count_matrix = np.zeros((max_x + 1, max_y + 1))
    print(count_matrix.shape)

    for x, y in arr_points:
        count_matrix[x][y] += 1
        print(f'elemento [{x}][{y}] : {count_matrix[x][y]}')

    dict_to_return = {}
    for x in range(max_x):
        for y in range(max_y):
            if count_matrix[x][y] >= 1:
                dict_to_return[(x, y)] = count_matrix[x][y]

    return dict_to_return
    # for key, value in dict_to_return.items():
    # print(f'la cella: {key} contiene {value} elementi')
