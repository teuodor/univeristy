from random import random
from random import randint
import numpy as np

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
    def __init__(self, nr_weights):
        self.output = 0
        self.weights = [random() for _ in range(nr_weights)]
        self.delta = 0

    def set_delta(self, delta):
        self.delta = delta

    def set_output(self, output):
        self.output = output


class Layer:
    def __init__(self, nr_neurons, nr_weights):
        self.neurons = [Neuron(nr_weights) for _ in range(nr_neurons)]


class Network:
    def __init__(self, nr_layers, classes, nr_neurons, dimensions):
        self.classes = classes
        self.output_layer = Layer(len(classes), nr_neurons + 1)
        self.hidden_layers = [Layer(nr_neurons + 1, dimensions)]
        self.hidden_layers += [Layer(nr_neurons + 1, nr_neurons + 1) for _ in range(nr_layers - 1)]

    def propagate_forward(self, inputs):
        for neuron in self.hidden_layers[0].neurons:
            neuron.set_output(sigmoid(activation(neuron.weights, inputs)))

        data = [neuron.output for neuron in self.hidden_layers[0].neurons]
        for layer in self.hidden_layers[1:]:
            for neuron in layer.neurons:
                neuron.set_output(sigmoid(activation(neuron.weights, data)))

            data = [neuron.output for neuron in layer.neurons]

        for neuron in self.output_layer.neurons:
            neuron.set_output(sigmoid(activation(neuron.weights, data)))

    def propagate_backward(self, expected):
        index = self.classes.index(expected)
        expected_output = [0] * len(self.classes)
        expected_output[index] = 1

        i = 0
        for neuron in self.output_layer.neurons:
            neuron.set_delta((expected_output[i] - neuron.output) * derivative_sigmoid(neuron.output))
            i += 1

        last_layer = self.output_layer
        for layer in reversed(self.hidden_layers):
            for i in range(len(layer.neurons)):
                layer.neurons[i].set_delta(derivative_sigmoid(layer.neurons[i].output) * sum(
                    [last_layer.neurons[j].delta * last_layer.neurons[j].weights[i] for j in range(len(last_layer.neurons))]
                ))
            last_layer = layer

    def update_weights(self, inputs):
        last_outputs = inputs
        for layer in self.hidden_layers:
            for neuron in layer.neurons:
                for i in range(len(neuron.weights)):
                    neuron.weights[i] += LEARNING_RATE * neuron.delta * last_outputs[i]
            last_outputs = [neuron.output for neuron in layer.neurons]

        for neuron in self.output_layer.neurons:
            for i in range(len(neuron.weights)):
                neuron.weights[i] += LEARNING_RATE * neuron.delta * last_outputs[i]

    def train(self):
        for iteration in range(ITERATIONS):
            loss = 0
            for i in range(len(training_x)):
                self.propagate_forward(training_x[i])
                self.propagate_backward(training_y[i])
                self.update_weights(training_x[i])
                expected = [0] * len(self.classes)
                index = self.classes.index(training_y[i])
                expected[index] = 1
                loss += sum([(expected[j] - self.output_layer.neurons[j].output) ** 2 for j in range(len(self.output_layer.neurons))])
            print("Epoch: " + str(iteration) + "  loss: " + str(loss))

        acc = 0.0
        for i in range(len(test_x)):
            self.propagate_forward(test_x[i])
            outputs = [neuron.output for neuron in self.output_layer.neurons]
            index = outputs.index(max(outputs))

            if test_y[i] == self.classes[index]:
                acc += 1.0
        acc /= len(test_x)
        print("Accuracy: " + str(acc))


network = Network(4, labels, 16, 5)
network.train()
