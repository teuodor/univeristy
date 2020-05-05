import copy
from random import randint


def random_permutation(n):
    permutation = [i for i in range(n)]
    index1 = randint(0, n - 1)
    index2 = randint(0, n - 1)
    permutation[index1], permutation[index2] = permutation[index2], permutation[index1]
    return permutation


class Chromosome:
    def _init_(self):
        self.__param = None
        self.__representation = None
        self.__fitness = 0.0

    def representation(self):
        return self.__representation

    def fitness(self):
        return self.__fitness

    def set_representation(self, representation):
        if representation is None:
            representation = []

        self.__representation = representation

    def set_fitness(self, fitness=0.0):
        self.__fitness = fitness

    def param(self, param):
        self.__param = param
        self.set_representation(random_permutation(self.__param['nr_nodes']))

    def crossover(self, other):
        index1 = randint(0, self.__param['nr_nodes'] - 1)
        index2 = randint(0, self.__param['nr_nodes'] - 1)

        if index2 < index1:
            index2, index1 = index1, index2

        new_representation = self.__representation[index1:index2]

        i = 0
        for el in other.representation()[index2:] + other.representation()[:index2]:
            if el not in new_representation:
                if len(new_representation) < self.__param['nr_nodes']:
                    new_representation.append(el)
                else:
                    new_representation.insert(i, el)
                    i += 1

        chromosome = Chromosome()
        chromosome.param(self.__param)
        chromosome.set_representation(new_representation)

        return chromosome

    def mutate(self):
        index1 = randint(0, self.__param['nr_nodes'] - 1)
        index2 = randint(0, self.__param['nr_nodes'] - 1)

        if index2 < index1:
            index2, index1 = index1, index2

        el = copy.deepcopy(self.__representation[index2])
        self.__representation.remove(self.__representation[index2])
        self.__representation.insert(index1 + 1, el)

    def __str__(self):
        return "Chromosome: " + str(self.__param) + " " + str(self.__fitness)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.__representation == other.representation()
