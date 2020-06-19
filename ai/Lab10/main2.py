from random import random
import numpy as np
import matplotlib.pyplot as plt

ITERATIONS = 300
LEARNING_RATE = 0.1
training_x = []
training_y = []
test_x = []
test_y = []


def sigmoid(x):
    if x < 0:
        return 1 - 1 / (1 + np.exp(x))
    else:
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

class Neuron:
    def __init__(self):
        self.weights = []
        self.delta = 0
        self.output = 0

    def push_back_weight(self, param):
        self.weights.append(param)

    def output_from_inputs(self, inputs):
        my_sum = self.weights[-1]
        for i in range(len(inputs)):
            my_sum += self.weights[i] * inputs[i]

        self.output = sigmoid(my_sum)

    def output_from_layer(self, list_of_neurons):
        my_sum = 0.0
        for i in range(len(list_of_neurons)):
            my_sum += self.weights[i] * list_of_neurons[i].output

        self.output = sigmoid(my_sum)

    def set_delta(self, delta):
        self.delta = delta

    def set_weights(self, index, param):
        self.weights[index] = param


class Network:
    def __init__(self, nr_of_layers, nr_of_neurons):
        self.layers = []
        self.nr_of_neurons = nr_of_neurons
        for q in range(nr_of_layers):
            neurons = []
            for i in range(nr_of_neurons):
                neurons.append(Neuron())
            self.layers.append(neurons)
        self.labels = labels
        self.error = 0.0

    def initialize(self, nr_of_inputs):
        first_layer = self.layers[0]
        for neuron in first_layer:
            for i in range(nr_of_inputs + 1):
                neuron.push_back_weight(0)

        nr_of_outputs = len(self.labels)
        last_layer = []
        for i in range(nr_of_outputs):
            last_layer.append(Neuron())

        self.layers.append(last_layer)
        for i in range(1, len(self.layers)):
            layer = self.layers[i]
            for neuron in layer:
                for j in range(self.nr_of_neurons):
                    neuron.push_back_weight(random())

    def propagation_forward(self, inputs):
        for neuron in self.layers[0]:
            neuron.output_from_inputs(inputs)

        for i in range(1, len(self.layers)):
            layer = self.layers[i]
            for neuron in layer:
                neuron.output_from_layer(self.layers[i - 1])

    def calculate_error(self, out):
        layer = self.layers[-1]
        for i in range(len(self.layers[-1])):
            if self.labels[i] == out:
                error = (1 - layer[i].output)
            else:
                error = (-layer[i].output)
            layer[i].set_delta(error * derivative_sigmoid(layer[i].output))

    def propagate_backward(self):
        for i in range(len(self.layers) - 2, -1, -1):
            layer = self.layers[i]
            for q in range(0, len(layer)):
                error = 0.0
                for neuron in self.layers[i + 1]:
                    error += neuron.weights[q] * neuron.delta
                layer[q].set_delta(error * derivative_sigmoid(layer[q].output))

    def update_weights(self, inputs):
        nr = len(inputs)
        for neuron in self.layers[0]:
            value = neuron.weights[nr]
            value += (LEARNING_RATE * neuron.delta)
            neuron.set_weights(nr, value)
            for i in range(0, len(inputs)):
                value = neuron.weights[i]
                value += (LEARNING_RATE * neuron.delta * inputs[i])
                neuron.set_weights(i, value)

        for j in range(1, len(self.layers)):
            layer = self.layers[j]
            last_layer = self.layers[j - 1]
            for neuron in layer:
                for i in range(len(last_layer)):
                    value = neuron.weights[i]
                    value += last_layer[i].output * LEARNING_RATE * neuron.delta
                    neuron.set_weights(i, value)

    def try_to_fit(self, inputs, out):
        self.propagation_forward(inputs)

        i = 0
        for neuron in self.layers[-1]:
            if out == self.labels[i]:
                v = 1
            else:
                v = 0
            self.error += (v - neuron.output) ** 2
            i += 1
        self.calculate_error(out)
        self.propagate_backward()
        self.update_weights(inputs)

    def fit(self, inputs, outputs):
        self.initialize(len(inputs[0]))
        x = []
        y = []
        for i in range(ITERATIONS):
            x.append(i)
            self.error = 0.0
            for j in range(len(inputs)):
                self.try_to_fit(inputs[j], outputs[j])
            y.append(self.error)
            print("Epoch: " + str(i) + " error: " + str(self.error))
        plt.plot(x, y)
        plt.show()

    def accuracy(self, test_inputs, test_outputs):
        acc = 0.0
        output = []
        for i in range(len(test_inputs)):
            self.propagation_forward(test_inputs[i])
            maxim = -1
            la = ""
            for j in range(len(self.layers[-1])):
                last_neuron = self.layers[-1][j]
                if maxim < last_neuron.output:
                    maxim = last_neuron.output
                    la = self.labels[j]
            output.append(la)
            if la == test_outputs[i]:
                acc += 1
        print("Accuracy: " + str(acc / len(test_inputs)))
        print(output)


network = Network(2, 10)
network.fit(training_x, training_y)
network.accuracy(training_x, training_y)
print(training_y)
