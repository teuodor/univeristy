import os
import csv
from random import random
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import numpy as np
from sklearn.linear_model import SGDRegressor

HAPPINESS = 2
GDP = 5
FREEDOM = 8
GENEROSITY = 9
TRUST = 10

ITERATIONS = 1000
LEARNING_RATE = 0.0001

dimensions = [GDP, FREEDOM]


def normalization_single(inputs):
    mean = 0.0
    deviation = 0.0

    for i in range(len(inputs)):
        mean += inputs[i]
    mean /= len(inputs)

    for i in range(len(inputs)):
        deviation += (inputs[i] - mean) ** 2

    deviation /= len(inputs)
    deviation = np.math.sqrt(deviation)

    for i in range(len(inputs)):
        inputs[i] = (inputs[i] - mean) / deviation


def normalization_multi_target(inputs):
    mean = [0.0] * len(inputs[0])
    deviation = [0.0] * len(inputs[0])

    for input_ in inputs:
        for i in range(len(input_)):
            mean[i] += input_[i]

    for i in mean:
        i /= len(mean)

    for input_ in inputs:
        for i in range(len(input_)):
            deviation[i] += (input_[i] - mean[i]) ** 2

    for i in deviation:
        i /= len(deviation)
        i = np.math.sqrt(i)

    for i in range(len(inputs)):
        for j in range(len(inputs[i])):
            inputs[i][j] = (inputs[i][j] - mean[j]) / deviation[j]


def get_y(betas, x):
    to_return = betas[0]
    for i in range(len(x)):
        to_return += betas[i + 1] * x[i]
    return to_return


def load_data(list_dimensions):
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

    # matrix_x = [[1, float(line[GDP]), float(line[FREEDOM])] for line in data]

    matrix_x = []
    matrix_y = [float(line[HAPPINESS]) for line in data]

    for line in data:
        x = []
        for dimension in list_dimensions:
            x.append(float(line[dimension]))
        matrix_x.append(x)

    return matrix_x, matrix_y, data


def training_set():
    _training_x = []
    _training_y = []
    _test_x = []
    _test_y = []
    matrix_x, matrix_y, data = load_data(dimensions)

    q = 0.8
    for i in range(0, len(data)):
        q0 = random()
        if q0 < q:
            _training_x.append(matrix_x[i])
            _training_y.append(matrix_y[i])
        else:
            _test_x.append(matrix_x[i])
            _test_y.append(matrix_y[i])

    # normalization_multi_target(_training_x)
    # normalization_single(_training_y)
    return _training_x, _training_y, _test_x, _test_y


training_x, training_y, test_x, test_y = training_set()


def error(betas, x, y):
    error_return = betas[0]
    for i in range(len(x)):
        error_return += betas[i + 1] * x[i]

    return error_return - y


def gradient_descent_no_tool():
    betas = []
    betas_inside = []
    for i in range(len(dimensions) + 1):
        betas_inside.append(random())
    betas.append(betas_inside)

    x = []
    for i in range(len(training_x[0])):
        average = 0.0
        for j in range(len(training_x)):
            average += training_x[j][i]
        x.append(average/len(training_x))

    y = sum(training_y) / len(training_y)

    for iteration in range(ITERATIONS):
        betas.append([0.0] * (len(dimensions) + 1))
        for j in range(len(training_x)):

            error_value = error(betas[iteration], x, y)
            for i in range(len(x)):
                betas[iteration + 1][i + 1] = betas[iteration][i + 1] - LEARNING_RATE * error_value * x[i]

    return betas


def gradient_descent_not_tool2():
    # betas = [[random() * training_x[0][i] for i in range(len(training_x[0]))]]
    # betas[0].append(0)
    betas = [[0.0] * (len(training_x[0]) + 1)]
    x = []
    for i in range(len(training_x[0])):
        average = 0.0
        for j in range(len(training_x)):
            average += training_x[j][i]
        x.append(average / len(training_x))

    for k in range(ITERATIONS):
        betas.append([0.0 for i in range(len(training_x[0]) + 1)])
        computed_output = [get_y(betas[k], training_x[i]) for i in range(len(training_x))]

        computed_error = 0.0
        for i in range(len(computed_output)):
            computed_error += (computed_output[i] - training_y[i])

        betas[k+1][0] = betas[k][0] - LEARNING_RATE*computed_error

        for i in range(len(x)):
            betas[k+1][i+1] = betas[k][i+1] - LEARNING_RATE * computed_error * x[i]

    print(betas[len(betas) - 1])
    return betas


def loss(betas):
    loss_list = []
    pred_y = []
    if len(betas) > len(dimensions) + 1:
        for i in range(ITERATIONS):
            loss_value = 0.0
            for j in range(0, len(training_x)):
                x_x = [x for x in training_x[j]]
                y = get_y(betas[i], x_x)
                loss_value += (training_y[j] - y) ** 2
                if i == ITERATIONS - 1:
                    pred_y.append(y)
            loss_list.append(loss_value)
        print(loss_value)
    else:
        for j in range(0, len(training_x)):
            x_x = [x for x in training_x[j]]
            y = get_y(betas, x_x)
            pred_y.append(y)

    return pred_y, loss_list


def graphic_loss(loss_list):
    plt1.ylabel('Loss')
    plt1.xlabel('batch')
    plt1.plot(loss_list, 'blue')
    plt1.show()


def plot(training1, training2, predicted, betas):
    if len(dimensions) == 2:
        ax = plt.axes(projection="3d")
        z_line = [training2[i] for i in range(len(training2))]
        y_line = [training1[i][1] for i in range(len(training1))]
        x_line = [training1[i][0] for i in range(len(training1))]
        ax.scatter3D(x_line, y_line, z_line, c='red')

        z_line1 = [predicted[i] for i in range(len(predicted))]
        y_line1 = [training1[i][1] for i in range(len(training1))]
        x_line1 = [training1[i][0] for i in range(len(training1))]
        ax.scatter3D(x_line1, y_line1, z_line1, c="purple")

        min_x = min(x_line)
        min_y = min(y_line)
        max_x = max(x_line)
        max_y = max(y_line)

        points_x = np.linspace(min_x, max_x, 10)
        points_y = np.linspace(min_y, max_y, 10)

        points_xx, points_yy = np.meshgrid(points_x, points_y)
        if len(betas) > 4:
            points_zz = betas[len(betas) - 1][1] * points_xx + betas[len(betas) - 1][2] * points_yy + betas[len(betas) - 1][0]
        else:
            points_zz = betas[1] * points_xx + betas[2] * points_yy + betas[0]

        ax.plot_surface(points_xx, points_yy, points_zz, alpha=0.7)

        ax.set_title("Happiness")
        ax.set_xlabel('GDP')
        ax.set_ylabel('Freedom')
        ax.set_zlabel('Happiness')
        plt.show()


n = gradient_descent_not_tool2()
plot(training_x, training_y, loss(n)[0], n)
graphic_loss(loss(n)[1])


def gradient_descent_tool():
    clf = SGDRegressor()

    for i in range(ITERATIONS):
        clf.partial_fit(training_x, training_y)

    print([x for x in clf.intercept_] + [x for x in clf.coef_])
    return [x for x in clf.intercept_] + [x for x in clf.coef_]


n = gradient_descent_tool()
#plot(training_x, training_y, graph_loss(n), n)

