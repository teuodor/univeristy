from random import random
import numpy as np
from sklearn.neural_network import MLPClassifier

ITERATIONS = 1000
LEARNING_RATE = 0.3
training_x = []
training_y = []
test_x = []
test_y = []


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def derivative_sigmoid(x):
    return x * (1.0 - x)


def activation(weights, inputs):
    to_return = 0
    for i in range(len(weights)):
        to_return = weights[i] * inputs[i]

    return to_return


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

for thai in range(len(training_x)):
    training_x[thai].append(1.0)
for thai in range(len(test_x)):
    test_x[thai].append(1.0)


class Neuron:
    def __init__(self, weights, data):
        self.weights = weights
        self.data = data
        self.delta = 0

    def set_data(self, data):
        self.data = data

    def set_delta(self, delta):
        self.delta = delta


class Network:
    def __init__(self, n_hidden_layers, n_neurons, dimensions, classes):
        n_outputs = len(classes)
        n_neurons = n_neurons
        self.hidden_layers = []
        for i in range(n_hidden_layers):
            if i == 0:
                inside = []
                for j in range(n_neurons):
                    weights = []
                    for k in range(dimensions):
                        weights.append(random())
                    inside.append(Neuron(weights, 0))
                self.hidden_layers.append(inside)
            else:
                inside = []
                for j in range(n_neurons):
                    weights = []
                    for k in range(n_neurons):
                        weights.append(random())
                    inside.append(Neuron(weights, 0))
                self.hidden_layers.append(inside)

        self.outputs = []

        for j in range(n_outputs):
            weights = []
            for k in range(n_neurons):
                weights.append(random())
            self.outputs.append(Neuron(weights, 0))

        self.classes = classes

    def front_propagate(self, inputs):
        for i in range(len(self.hidden_layers)):
            if i == 0:
                for j in range(len(self.hidden_layers[i])):
                    data = sigmoid(activation(self.hidden_layers[i][j].weights, inputs))
                    self.hidden_layers[i][j].set_data(data)
            else:
                datas = [self.hidden_layers[i - 1][j].data for j in range(len(self.hidden_layers[i - 1]))]
                for j in range(len(self.hidden_layers[i])):
                    data = sigmoid(activation(self.hidden_layers[i][j].weights, datas))
                    self.hidden_layers[i][j].set_data(data)

        datas = [self.hidden_layers[-1][i].data for i in range(len(self.hidden_layers[-1]))]
        for i in range(len(self.outputs)):
            data = sigmoid(activation(self.outputs[i].weights, datas))
            self.outputs[i].set_data(data)

    def back_propagate(self, expected):
        index_class = 0
        for class_ in range(len(self.classes)):
            if self.classes[class_] == expected:
                index_class = class_
        expected = [0] * len(self.classes)
        expected[index_class] = 1
        outputs = [self.outputs[i].data for i in range(len(self.outputs))]

        error_outputs = [(expected[i] - outputs[i]) * derivative_sigmoid(outputs[i]) for i in range(len(expected))]

        for i in range(len(self.outputs)):
            self.outputs[i].set_delta(error_outputs[i])

        for i in reversed(range(len(self.hidden_layers))):
            errors = list()
            if i != len(self.hidden_layers) - 1:
                for j in range(len(self.hidden_layers[i])):
                    error = 0
                    for k in range(len(self.hidden_layers[i + 1])):
                        error += self.hidden_layers[i + 1][k].weights[j] * self.hidden_layers[i + 1][k].delta
                    errors.append(error)
            else:
                for k in range(len(self.hidden_layers[i])):
                    error = 0.0
                    for neuron in self.outputs:
                        error += neuron.weights[k] * neuron.delta
                    errors.append(error)
            for j in range(len(self.hidden_layers[i])):
                self.hidden_layers[i][j].set_delta(errors[j] * derivative_sigmoid(self.hidden_layers[i][j].data))

    def update_weights(self, inputs):
        outputs = [neuron.data for neuron in self.hidden_layers[-1]]

        for neuron in self.outputs:
            for i in range(len(neuron.weights)):
                neuron.weights[i] += LEARNING_RATE * neuron.delta * outputs[i]

        for i in range(len(self.hidden_layers)):
            outputs = inputs
            if i != 0:
                outputs = [neuron.data for neuron in self.hidden_layers[i - 1]]
            for neuron in self.hidden_layers[i]:
                for j in range(len(outputs)):
                    neuron.weights[j] += LEARNING_RATE * neuron.delta * outputs[j]


def initialize_network(n_hidden_layers, n_neurons, dimensions):
    nwrk = Network(n_hidden_layers, n_neurons, dimensions, labels)
    for iteration in range(ITERATIONS):
        sum_error = 0
        for i in range(len(training_x)):
            # if i == 1 or i == 51:
            #     print([neuron.data for neuron in nwrk.outputs])
            nwrk.front_propagate(training_x[i])
            outputs = [neuron.data for neuron in nwrk.outputs]
            expected = [0 for i in range(len(nwrk.outputs))]
            expected[nwrk.classes.index(training_y[i])] = 1
            sum_error += sum([(expected[k] - nwrk.outputs[k].data) ** 2 for k in range(len(expected))])
            nwrk.back_propagate(training_y[i])
            nwrk.update_weights(training_x[i])
        print("Epoch: " + str(iteration + 1) + " l_rate: " + str(LEARNING_RATE) +
              " error: " + str(sum_error))

    acc = 0.0
    for i in range(len(test_x)):
        nwrk.front_propagate(test_x[i])
        index = 0
        max_ = nwrk.outputs[0].data
        for j in range(len(nwrk.outputs)):
            if nwrk.outputs[j].data > max_:
                max_ = nwrk.outputs[j].data
                index = j
        if nwrk.classes[index] == test_y[i]:
            acc += 1
    acc /= len(test_x)
    print("Accuracy: " + str(acc))


initialize_network(1, 2, len(training_x[0]))


def tool():
    for x in training_x:
        x = x[:-1]

    for x in test_x:
        x = x[:-1]

    ml = MLPClassifier(random_state=1, max_iter=300)
    ml.fit(training_x, training_y)
    print("Accuracy tool: " + str(ml.score(test_x, test_y)))


tool()
