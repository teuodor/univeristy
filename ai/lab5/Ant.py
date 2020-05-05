import math
from random import randint, random

import numpy


class Ant:
    def __init__(self):
        self.__param = None
        self.__path = []
        self.__length = 0
        self.__pheromone_path = []

    def param(self, param):
        self.__param = param
        self.__path = [randint(0, self.__param['nr_nodes'] - 1)]
        self.__pheromone_path = [[0 for _ in range(self.__param['nr_nodes'])] for _ in range(self.__param['nr_nodes'])]

    def length(self):
        return self.__length

    def path(self):
        return self.__path

    def pheromone_path(self):
        return self.__pheromone_path

    def set_start(self, city):
        self.__path = [city]

    def get_next_node(self):
        denominator = 0.0
        choices = []
        current_node = self.__path[-1]

        nr_nodes = self.__param['nr_nodes']
        matrix = self.__param['matrix']
        pheromone_matrix = self.__param['pheromone_matrix']
        alpha = self.__param['alpha']
        beta = self.__param['beta']
        quantifier = self.__param['quantifier']

        for node in range(nr_nodes):
            if node not in self.__path:
                denominator += math.pow(1/matrix[current_node][node], alpha) * \
                            math.pow(pheromone_matrix[current_node][node], beta)
                choices.append(node)

        chosen_node = 0
        q = random()
        if q < quantifier:
            max_value = 0
            for node in choices:
                node_prob = math.pow(1 / matrix[current_node][node], alpha) * math.pow(pheromone_matrix[current_node][node], beta)
                if node_prob > max_value:
                    chosen_node = node
                    max_value = node_prob
        else:
            weights = []
            for node in choices:
                weight = math.pow(1 / matrix[current_node][node], alpha) * math.pow(pheromone_matrix[current_node][node], beta) / denominator
                weights.append(weight)

            chosen_node = numpy.random.choice(choices, 1, p=weights)[0]

        self.__path.append(chosen_node)
        self.__length += matrix[current_node][chosen_node]
        self.__pheromone_path[current_node][chosen_node] = 1
        self.__pheromone_path[chosen_node][current_node] = 1

        return current_node, chosen_node

    def return_start(self):
        self.__path.append(self.__path[0])
        self.__length += self.__param["matrix"][self.__path[-2]][self.__path[-1]]
        self.__pheromone_path[-2][-1] = 1
        self.__pheromone_path[-1][-2] = 1


def roulette(choices, weights):
    for i in range(len(choices) - 1):
        for j in range(i + 1, len(choices)):
            if weights[i] < weights[j]:
                weights[i], weights[j] = weights[j], weights[i]
                choices[i], choices[j] = choices[j], choices[i]

    for i in range(len(weights) - 1):
        for j in range(i + 1, len(weights)):
            weights[i] += weights[j]

    r = random()

    for i in range(0, len(weights) - 1):
        if weights[i] <= r <= weights[i + 1]:
            return choices[i]

    return choices[len(choices) - 1]
