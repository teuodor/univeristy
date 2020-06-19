from random import random
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing


training_x = []
test_x = []
training_y = []
test_y = []
loss = []

ITERATIONS = 2000
LEARNING_RATE = 0.01


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


def load_data():
    f = open("iris.data", 'r')
    line = f.readline()
    q = 0.8
    while line != "":
        split = line.split(",")
        inside_x = []
        q0 = random()
        for i in range(len(split)):
            if i == len(split) - 1:
                if q0 < q:
                    training_y.append(split[i].strip("\n"))
                else:
                    test_y.append(split[i].strip("\n"))
            else:
                inside_x.append(float(split[i]))
        if q0 < q:
            training_x.append(inside_x)
        else:
            test_x.append(inside_x)
        line = f.readline()


load_data()
labels = []
for label in training_y + test_y:
    if label not in labels:
        labels.append(label)

all_betas = []
for label in range(len(labels)):
    all_betas.append([])
# scaled_x = preprocessing.scale(training_x)
# training_x = scaled_x


def logistic_regression_tool():
    lr = LogisticRegression(max_iter=1000)
    lr.fit(training_x, training_y)
    print("accuracy: " + str(lr.score(test_x, test_y)))
    coef = lr.coef_
    intercept = lr.intercept_
    print(coef)
    print(intercept)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def computed_output(betas, x):
    to_return = betas[0]
    for i in range(len(x)):
        to_return += betas[i + 1] * x[i]
    return to_return


def my_logistic_regression_batch():
    betas = []
    for i in range(len(labels)):
        betas.append([0.0] * (len(training_x[0]) + 1))

    mean_x = [0.0] * len(training_x[0])
    for x in training_x:
        for j in range(len(x)):
            mean_x[j] += x[j]
    for x in range(len(mean_x)):
        mean_x[x] /= len(training_x)

    for iteration in range(ITERATIONS):
        for LABEL in range(len(labels)):
            new_y = [1 if y == labels[LABEL] else 0 for y in training_y]
            outputs = [sigmoid(computed_output(betas[LABEL], training_x[i])) for i in range(len(training_x))]

            error_value = 0.0
            for i in range(len(outputs)):
                error_value += (outputs[i] - new_y[i])

            betas[LABEL][0] = betas[LABEL][0] - LEARNING_RATE * error_value
            for i in range(len(mean_x)):
                betas[LABEL][i + 1] = betas[LABEL][i + 1] - LEARNING_RATE * error_value * mean_x[i]

    return betas


def graphic_loss(loss_list):
    for l in loss:
        plt.ylabel('Loss')
        plt.xlabel('batch')
        plt.plot(l)
    plt.show()


def my_logistic_regression_stochastic():
    betas = []
    for i in range(len(labels)):
        betas.append([0.0] * (len(training_x[0]) + 1))

    for l in range(len(labels)):
        loss.append([])

    for iteration in range(ITERATIONS):
        for LABEL in range(len(labels)):
            new_y = [1 if y == labels[LABEL] else 0 for y in training_y]
            error_value = 0
            for i in range(len(new_y)):
                output = sigmoid(computed_output(betas[LABEL], training_x[i]))
                error_value = output - new_y[i]

                betas[LABEL][0] = betas[LABEL][0] - LEARNING_RATE * error_value
                for j in range(len(training_x[i])):
                    betas[LABEL][j + 1] = betas[LABEL][j + 1] - LEARNING_RATE * error_value * training_x[i][j]
            loss[LABEL].append(error_value ** 2)
            all_betas[LABEL].append(betas[LABEL])

    graphic_loss(loss)

    return betas


def accuracy(betas):
    acc = 0
    for x in range(len(test_x)):
        outputs = []
        for LABEL in range(len(betas)):
            outputs.append(computed_output(betas[LABEL], test_x[x]))
        index = 0
        max_value = outputs[0]
        for i in range(1, len(outputs)):
            if outputs[i] > max_value:
                max_value = outputs[i]
                index = i
        if labels[index] == test_y[x]:
            acc += 1

    for i in betas:
        print(i)
    print("accuracy: " + str(acc / (len(test_x))))


# def loss():
#     loss_list = []
#     for i in range(len(labels)):
#         loss_list.append([])
#
#     for i in range(ITERATIONS):
#         for LABEL in range(len(labels)):
#             new_y = [1 if y == labels[LABEL] else 0 for y in training_y]
#             loss_value = 0.0
#             for j in range(len(test_y)):
#                 output = computed_output(all_betas[LABEL][i], training_x[j])
#                 loss_value += (output - new_y[j]) ** 2
#             loss_list[LABEL].append(loss_value)
#
#     plt.ylabel("Loss")
#     plt.xlabel("Batch")
#     for i in range(len(loss_list)):
#         plt.plot(loss_list[i])
#     plt.show()


logistic_regression_tool()
accuracy(my_logistic_regression_stochastic())
# loss()


