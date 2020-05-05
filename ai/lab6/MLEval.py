import numpy
import math


def _accuracy(real_labels, computed_labels):
    no_correct = 0
    for i in range(len(real_labels)):
        if real_labels[i] == computed_labels[i]:
            no_correct += 1

    return no_correct / len(real_labels)


def _precision(real_labels, computed_labels, elem):
    correct_computed = 0
    correct_predicted = 0

    for i in range(len(real_labels)):
        if computed_labels[i] == elem:
            correct_computed += 1
        if real_labels[i] == elem == computed_labels[i]:
            correct_predicted += 1

    return float(correct_predicted) / correct_computed


def _recall(real_labels, computed_labels, elem):
    correct_real = 0
    correct_predicted = 0

    for i in range(len(real_labels)):
        if real_labels[i] == elem:
            correct_real += 1
        if real_labels[i] == elem == computed_labels[i]:
            correct_predicted += 1

    return float(correct_predicted) / correct_real


def _labels_f(real_labels):
    labels_return = []
    for i in real_labels:
        if i not in labels_return:
            labels_return.append(i)

    return labels_return


class MLEval:
    def __init(self):
        pass

    @staticmethod
    def loss(self, real_labels, computed_labels):
        error = 0.0
        for i in real_labels:
            nr = 0
            index = list(set(real_labels)).index(real_labels[i])
            error += 1 - computed_labels[i][index] ** 2

        return error / len(set(real_labels))

    @staticmethod
    def eval_classification(real_labels, computed_outputs):
        labels = _labels_f(real_labels)

        computed_labels = [labels[numpy.argmax(p)] for p in computed_outputs]

        classifications = {'acc': _accuracy(real_labels, computed_labels),
                           'prec': [_precision(real_labels, computed_labels, label) for label in labels],
                           'rec': [_recall(real_labels, computed_labels, label) for label in labels]}

        return str(classifications)

    @staticmethod
    def prediction_error(real_labels, computed_outputs):
        error = 0.0
        labels = _labels_f(real_labels)
        for i in range(len(computed_outputs)):
            index = labels.index(real_labels[i])
            for j in range(len(computed_outputs[i])):
                if j == index:
                    error += 1 - computed_outputs[i][j]
                else:
                    error += computed_outputs[i][j]

        error *= 1/len(real_labels)

        return error

    @staticmethod
    def loss(real_labels, computed_outputs):
        error = 0.0
        labels = _labels_f(real_labels)
        for i in range(len(computed_outputs)):
            index = labels.index(real_labels[i])
            for j in range(len(computed_outputs[i])):
                if j == index:
                    error += (1 - computed_outputs[i][j]) ** 2
                else:
                    error += computed_outputs[i][j] ** 2

        error *= 1 / len(real_labels)
        error = math.sqrt(error)

        return error


