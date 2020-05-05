import os
import csv
from random import random
import matplotlib.pyplot as plt
import numpy as np

from Lab7.matrix import Matrix

HAPPINESS = 2
GDP = 5
FREEDOM = 8


def load_data():
    data = []
    labels = []
    file_path = os.path.join('2017.csv')
    with open(file_path) as file:
        csv_reader = csv.reader(file, delimiter=",")
        counter = 0
        for row in csv_reader:
            if counter == 0:
                labels = row
            else:
                data.append(row)
            counter += 1

    matrix_x = [[1, float(line[GDP]), float(line[FREEDOM])] for line in data]
    matrix_y = [[float(line[HAPPINESS])] for line in data]
    # for line in data:
    #     matrix_x.append([1, float(line[GDP]), float(line[FREEDOM])])
    #     matrix_y.append([float(line(HAPPINESS))])

    return matrix_x, matrix_y, data


def training_set():
    _training_x = []
    _training_y = []
    _test_x = []
    _test_y = []
    matrix_x, matrix_y, data = load_data()

    q = 0.9
    for i in range(0, len(data)):
        q0 = random()
        if q0 < q:
            _training_x.append(matrix_x[i])
            _training_y.append(matrix_y[i])
        else:
            _test_x.append(matrix_x[i])
            _test_y.append(matrix_y[i])

    return _training_x, _training_y, _test_x, _test_y


def get_y(b0, b1, x1, b2, x2):
    return b0 + b1*x1 + b2*x2


training_x, training_y, test_x, test_y = training_set()


def result_matrix():
    matrix = Matrix(training_x)
    transposed_matrix = Matrix(matrix.transposed())

    matrix_squared = Matrix(transposed_matrix.multiplication(matrix))
    reversed_matrix = Matrix(matrix_squared.reverse())
    result = Matrix(reversed_matrix.multiplication(transposed_matrix))

    return result.multiplication(Matrix(training_y))


def result_tool():
    matrix = np.array(training_x)
    transposed_x = np.array(np.transpose(training_x))
    multiplied_x = np.matmul(transposed_x, matrix)
    inverse_matrix = np.linalg.inv(multiplied_x)
    result = np.matmul(inverse_matrix, transposed_x)
    return np.matmul(result, training_y)


def loss():
    loss_value = 0
    result = result_matrix()
    b0 = result[0][0]
    b1 = result[1][0]
    b2 = result[2][0]
    pred_y = []
    for index in range(0, len(test_x)):
        x1 = test_x[index][1] * 1.0
        x2 = test_x[index][2] * 1.0
        predicted_y = get_y(b0, b1, x1, b2, x2)
        pred_y.append(predicted_y)
        loss_value += (test_y[index][0] - predicted_y) ** 2

    min_index = 0
    max_index = 0
    min_value = pred_y[0]
    max_value = pred_y[0]
    for i in range(1, len(pred_y)):
        if pred_y[i] > max_value:
            max_value = pred_y[i]
            max_index = i
        if pred_y[i] < min_value:
            min_value = pred_y[i]
            min_index = i

    plot(training_x, training_y, test_x, test_y, pred_y, min_index, max_index)

    print("Loss: " + str(loss_value))


def loss2():
    loss2_value = 0
    result = result_tool()
    print(result)
    b0 = result[0][0]
    b1 = result[1][0]
    b2 = result[2][0]
    pred_y = []
    for index in range(0, len(test_x)):
        x1 = test_x[index][1] * 1.0
        x2 = test_x[index][2] * 1.0
        predicted_y = get_y(b0, b1, x1, b2, x2)
        pred_y.append(predicted_y)
        loss2_value += (test_y[index][0] - predicted_y) ** 2

    min_index = 0
    max_index = 0
    min_value = pred_y[0]
    max_value = pred_y[0]
    for i in range(1, len(pred_y)):
        if pred_y[i] > max_value:
            max_value = pred_y[i]
            max_index = i
        if pred_y[i] < min_value:
            min_value = pred_y[i]
            min_index = i

    print(training_x)
    print(training_y)
    print(test_x)
    print(test_y)
    print(pred_y)

    plot(training_x, training_y, test_x, test_y, pred_y, min_index, max_index)

    print("Loss: " + str(loss2_value))


def plot(training1, training2, test1, test2, predicted, min_index, max_index):
    ax = plt.axes(projection="3d")
    z_line = [training2[i][0] for i in range(len(training2))]
    y_line = [training1[i][2] for i in range(len(training1))]
    x_line = [training1[i][1] for i in range(len(training1))]
    ax.scatter3D(x_line, y_line, z_line, c='red')

    z_line = [test2[i][0] for i in range(len(test2))]
    y_line = [test1[i][2] for i in range(len(test1))]
    x_line = [test1[i][1] for i in range(len(test1))]
    ax.scatter3D(x_line, y_line, z_line, c='blue')

    xs = [test1[min_index][1], test1[max_index][1]]
    ys = [predicted[min_index], predicted[max_index]]
    zs = [test2[min_index][0], test2[max_index][0]]
    ax.plot(xs, ys, zs)

    # xs = [test1[min_index][1], test1[max_index][1]]
    # ys = [predicted[min_index], predicted[max_index]]
    # zs = [0, 0]
    # ax.plot(xs, ys, zs)
    ax.set_title("Happiness")
    ax.set_xlabel('GDP')
    ax.set_ylabel('Freedom')
    ax.set_zlabel('Happiness')
    plt.show()


loss()
loss2()
